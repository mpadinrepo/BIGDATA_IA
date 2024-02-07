import numpy as np
from Tarefa58 import obtener_elementos_en_la_misma_posicion, obtener_numeros_entre_5_y_10, maxx, normalizar_sepallength

def test_obtener_elementos_en_la_misma_posicion():
    a = np.array([1,2,3,2,3,4,3,4,5,6])
    b = np.array([7,2,10,2,7,4,9,4,9,8])
    resultado = obtener_elementos_en_la_misma_posicion(a, b)
    assert np.array_equal(resultado, np.array([2, 2, 4, 4]))

def test_obtener_numeros_entre_5_y_10():
    a = np.array([2, 6, 1, 9, 10, 3, 27])
    resultado = obtener_numeros_entre_5_y_10(a)
    assert np.array_equal(resultado, np.array([6, 9, 10]))

def test_maxx():
    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])
    resultado = maxx(a, b)
    assert np.array_equal(resultado, np.array([6, 7, 9, 8, 9, 7, 5]))

def test_normalizar_sepallength():
    ruta_archivo = "/media/DIURNO/CURSO/PIA_ISAAC/Ud2 Python/TarefazPIA/Tarefa58/iris.data"
    sepallength_normalizado = normalizar_sepallength(ruta_archivo)
    assert np.all(sepallength_normalizado >= 0) and np.all(sepallength_normalizado <= 1)