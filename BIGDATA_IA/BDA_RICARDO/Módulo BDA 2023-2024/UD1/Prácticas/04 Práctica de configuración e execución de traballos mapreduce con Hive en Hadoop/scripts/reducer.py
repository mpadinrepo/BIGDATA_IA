#!/usr/bin/python3

import sys

# Inicializa variables para almacenar el total de cantidad para cada producto
current_product = None
current_count = 0

# Lee cada línea de entrada
for line in sys.stdin:
    # Elimina espacios en blanco al principio y al final, y divide la línea en clave y valor
    line = line.strip()
    product, count = line.split('\t', 1)

    # Si el producto actual es diferente al producto procesado anteriormente,
    # imprime el resultado acumulado hasta el momento y reinicia las variables
    if current_product and current_product != product:
        print(f"{current_product}\t{current_count}")
        current_count = 0

    # Actualiza el producto actual y suma la cantidad al contador
    current_product = product
    current_count += int(count)

# Imprime el último resultado
if current_product:
    print(f"{current_product}\t{current_count}")
