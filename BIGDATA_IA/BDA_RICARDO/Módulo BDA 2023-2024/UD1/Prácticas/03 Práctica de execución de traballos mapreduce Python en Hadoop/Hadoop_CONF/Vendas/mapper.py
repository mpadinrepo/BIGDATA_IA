#!/usr/bin/env python
import sys

def mapper():
    for line in sys.stdin:
        # Eliminar espacios en blanco al principio y al final y dividir la línea en campos
        fields = line.strip().split("\t")
        
        # Verificar si hay campos y que haya exactamente 5
        if len(fields) == 5:
            # Emitir la línea al reducer
            print('\t'.join(fields))

if __name__ == "__main__":
    mapper()

