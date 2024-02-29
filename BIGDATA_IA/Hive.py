CREATE TABLE purchases (
    date STRING,
    store STRING,
    payment_type STRING,
    category STRING,
    amount FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;


LOAD DATA INPATH '/ruta/al/archivo/purchases.txt' OVERWRITE INTO TABLE purchases;


-- 1. Número total de ventas
SELECT COUNT(*) AS total_sales FROM purchases;

-- 2. Importe total de ventas
SELECT SUM(amount) AS total_amount FROM purchases;

-- 3. Suma total y número de ventas por tienda
SELECT store, SUM(amount) AS total_amount, COUNT(*) AS total_sales
FROM purchases
GROUP BY store;

-- 4. Venta mínima por tipo de pago
SELECT payment_type, MIN(amount) AS min_sale
FROM purchases
GROUP BY payment_type;

-- 5. Media de ventas por tienda
SELECT store, AVG(amount) AS avg_sale
FROM purchases
GROUP BY store;

-- 6. Tiendas por encima de la media en ventas
SELECT store
FROM (
    SELECT store, AVG(amount) AS avg_sale
    FROM purchases
    GROUP BY store
) sub
WHERE amount > avg_sale;

-- 7. Tipo de pago más utilizado
SELECT payment_type, COUNT(*) AS total_sales
FROM purchases
GROUP BY payment_type
ORDER BY total_sales DESC
LIMIT 1;

-- 8. Datos de las 25 ventas más altas (fecha, tienda, venta, categoría)
SELECT date, store, amount, category
FROM purchases
ORDER BY amount DESC
LIMIT 25;

-- 9. Listado de tiendas con mayor número de ventas en cada categoría
SELECT category, store, COUNT(*) AS total_sales
FROM (
    SELECT category, store
    FROM purchases
    GROUP BY category, store
) sub
WHERE ROW_NUMBER() OVER (PARTITION BY category ORDER BY total_sales DESC) = 1;

-- 10. Bonus: Top N de ventas por tienda
SELECT date, store, amount, category
FROM (
    SELECT date, store, amount, category,
           RANK() OVER (PARTITION BY store ORDER BY amount DESC) AS ranking
    FROM purchases
) ranked_sales
WHERE ranking <= N;

-- 11. Guardar en HDFS las ventas de juguetes con valores mayores de 200
INSERT OVERWRITE DIRECTORY '/ruta/de/salida'
SELECT *
FROM purchases
WHERE category = 'toys' AND amount > 200;

-- 12. Repetir la consulta con salida separada por ';'
INSERT OVERWRITE DIRECTORY '/ruta/de/salida_separada_por_punto_y_coma'
SELECT CONCAT_WS(';', date, store, payment_type, category, amount)
FROM purchases;

-- 13. Guardar en disco local las ventas pagadas con Visa o MasterCard con salida separada por tabuladores
INSERT OVERWRITE LOCAL DIRECTORY '/ruta/de/salida_local_separada_por_tabuladores'
SELECT CONCAT_WS('\t', date, store, payment_type, category, amount)
FROM purchases
WHERE payment_type IN ('Visa', 'MasterCard');
