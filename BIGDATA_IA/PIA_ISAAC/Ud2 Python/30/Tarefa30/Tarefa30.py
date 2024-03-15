# Escribir unha función que calcule a área dun círculo
# e outra que calcule o volume dun cilindro usando a primeira función.
# A area do círculo é pi*r**2
# O volume do cilindro é  pi*r**2 * h
""" 
import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area
radio_do_circulo = 5
area_calculada = calcular_area_do_circulo(raio_do_circulo)
print(f"A área do círculo com raio {raio_do_circulo} é {area_calculada}")
 """

import math


radio_circulo = int(input('Escriba cuanto mide el radio del circulo :'))
altura_cilindro = int(input('Escriba cuanto mide la altura del cilindro :'))



def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area


def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen


area_calculada = calcular_area_circulo(radio_circulo)
volumen_calculado = calcular_volumen_cilindro(radio_circulo, altura_cilindro)

print(f"El área del círculo con radio de valor {radio_circulo} es {area_calculada}")
print(f"El volumen del cilindro con radio de valor {radio_circulo} y altura {altura_cilindro} es {volumen_calculado}")
