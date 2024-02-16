#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def reducer():
    current_year = None
    max_rainfall = None

    for line in sys.stdin:
        # Eliminar espacios en blanco al principio y al final de la línea
        line = line.strip()
        
        # Dividir la línea en campos separados por tabuladores
        parts = line.split("\t")
        
        # Verificar que haya suficientes campos
        if len(parts) != 2:
            continue  # Ignorar líneas que no tienen el formato esperado
        
        # Extraer el año y la cantidad de lluvia
        year, rainfall = parts
        
        # Verificar si el año es válido y el código de validación es 1 o 5
        if year.isdigit() and (rainfall.replace('.', '', 1).isdigit() or rainfall.replace(',', '', 1).isdigit()):
            year = year.strip('"').split('-')[0]  # Truncar la fecha para obtener solo el año
            rainfall = float(rainfall.replace(',', '.'))  # Reemplazar coma por punto para que sea un número válido
            
            # Si el año actual es igual al año del registro actual
            if current_year == year:
                # Actualizar la máxima cantidad de lluvia si es necesario
                max_rainfall = max(max_rainfall, rainfall)
            else:
                # Si es un año diferente, imprimir el año anterior y su máxima cantidad de lluvia
                if current_year is not None:
                    print(f"{current_year}\t{max_rainfall}")
                # Actualizar el año actual y la máxima cantidad de lluvia
                current_year = year
                max_rainfall = rainfall

    # Imprimir la solución del último año
    if current_year is not None:
        print(f"{current_year}\t{max_rainfall}")

if __name__ == "__main__":
    reducer()

