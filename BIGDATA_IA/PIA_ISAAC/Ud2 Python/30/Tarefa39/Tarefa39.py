""" Tarefa 39

Escribir un programa que cree un dicionario simulando unha cesta da compra. 
O programa debe preguntar 
o artigo
o seu prezo
e engadir o par ao dicionario, ata que o usuario decida terminar. 

Despois débese mostrar por pantalla a lista da compra e o custo total, co seguinte formato
Lista da compra    
Artigo 1     Prezo
Artigo 2     Prezo
Artigo 3     Prezo
…     …
Total     Custo """

# Inicializar el diccionario de la cesta de la compra
cesta_compra = {}

# Bucle para añadir artículos a la cesta
while True:
    # Pedir al usuario el artículo y su precio
    articulo = input("Introduce el nombre del artículo (o 'fin' para terminar): ")
    
    # Comprobar si el usuario quiere terminar
    if articulo.lower() == 'fin':
        break
    
    precio = float(input(f"Introduce el precio del {articulo}: "))
    
    # Añadir el artículo y su precio a la cesta
    cesta_compra[articulo] = precio

# Mostrar la lista de la compra y el costo total
print("\nLista de la compra")
costo_total = 0

for articulo, precio in cesta_compra.items():
    print(f"{articulo:10}  {precio}")
    costo_total += precio

print(f"\nTotal{'':10}\n{costo_total}")
