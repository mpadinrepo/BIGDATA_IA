#!/usr/bin/env python3

import sys

# Leer la primera línea y dividirla en los nombres de las columnas
header = sys.stdin.readline().strip().split("\t")

# Iterar sobre cada línea de la entrada estándar
for line in sys.stdin:
    # Eliminar espacios en blanco al principio y al final de la línea
    line = line.strip()
    
    # Dividir la línea en campos separados por tabuladores
    fields = line.split("\t")
    
    # Verificar que haya suficientes campos
    if len(fields) == len(header):
        # Crear un diccionario con los nombres de las columnas como clave y los valores de la línea como valor
        record = dict(zip(header, fields))
        
        # Imprimir el diccionario como salida, lo que dará un formato clave-valor
        print(record)

