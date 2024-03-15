#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# Parte 3: Total de ventas por categoría de producto
# Parte 4: Venta más alta por tipo de pago
# Parte 5: Máximo absoluto de todas las ventas
# Parte 6: Total de ventas

# Configurar variables para cada parte
total_sales_per_category = {}
max_sales_per_payment = {}
max_absolute_sale = 0
total_sales = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data

        # Parte 3: Total de ventas por categoría de producto
        total_sales_per_category[item] = total_sales_per_category.get(item, 0) + float(cost)

        # Parte 4: Venta más alta por tipo de pago
        if payment not in max_sales_per_payment or float(cost) > max_sales_per_payment[payment]:
            max_sales_per_payment[payment] = float(cost)

        # Parte 5: Máximo absoluto de todas las ventas
        max_absolute_sale = max(max_absolute_sale, float(cost))

        # Parte 6: Total de ventas
        total_sales += float(cost)

# Imprimir resultados combinados
for category, total in total_sales_per_category.items():
    print('Categoría: {}\tTotal de ventas: {}'.format(category, total))

for payment, max_sale in max_sales_per_payment.items():
    print('Tipo de pago: {}\tVenta más alta: {}'.format(payment, max_sale))

print('Máximo absoluto de todas las ventas: {}'.format(max_absolute_sale))

print('Total de ventas: {}'.format(total_sales))
