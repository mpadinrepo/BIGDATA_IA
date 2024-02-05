# test_Tarefa41.py
from Tarefa41 import calcular_area_circulo, calcular_volumen_cilindro
import math  # Agregamos la importación del módulo math

def test_calcular_area_circulo():
    assert calcular_area_circulo(1) == math.pi
    assert calcular_area_circulo(2) == 4 * math.pi
    assert calcular_area_circulo(0) == 0

def test_calcular_volumen_cilindro():
    assert calcular_volumen_cilindro(1, 1) == math.pi
    assert calcular_volumen_cilindro(2, 3) == 12 * math.pi
    assert calcular_volumen_cilindro(0, 5) == 0
