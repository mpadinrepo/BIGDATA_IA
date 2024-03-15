#!/usr/bin/python3

import sys

# Lee cada línea de entrada
for line in sys.stdin:
    # Elimina espacios en blanco al principio y al final, y divide la línea en campos
    line = line.strip()
    fields = line.split(',')

    # Ignora las líneas que no tienen el formato esperado
    if len(fields) == 4:
        # Extrae los campos relevantes
        fecha, producto, cantidad, precio = fields

        # Emite la clave y el valor (clave: producto, valor: cantidad)
        print(f"{producto}\t{cantidad}")
