#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def mapper():
    for line in sys.stdin:
        line = line.strip()
        fields = line.split(",")
        codigo = fields[0].strip('"')
        data = fields[1].split()[0]  # Obtener solo el año de la fecha
        choiva = fields[4].strip('"')  # Eliminar comillas del valor de la lluvia
        
        if codigo in ["1", "5"]:
            print(f"{data}\t{choiva}")

if __name__ == "__main__":
    mapper()

