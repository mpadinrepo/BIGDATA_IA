#!/usr/bin/env python
import sys

def reducer():
    total_ventas = 0
    for line in sys.stdin:
        # Dividir la línea en campos
        fields = line.strip().split("\t")
        
        # Verificar si hay exactamente 5 campos
        if len(fields) == 5:
            # Incrementar el contador de ventas
            total_ventas += 1

    # Imprimir el total de ventas
    print("Total de ventas:", total_ventas)

if __name__ == "__main__":
    reducer()

