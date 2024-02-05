# Tarefa41.py
import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.

    Parámetros:
    - radio (float): Radio del círculo.

    Devuelve:
    float: Área del círculo.
    """
    area = math.pi * radio ** 2
    return area

def calcular_volumen_cilindro(radio, altura):
    """
    Calcula el volumen de un cilindro.

    Parámetros:
    - radio (float): Radio del cilindro.
    - altura (float): Altura del cilindro.

    Devuelve:
    float: Volumen del cilindro.
    """
    volumen = math.pi * radio ** 2 * altura
    return volumen
