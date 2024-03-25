# test_programa.py

import Tarefa7

def test_obtener_info_nombre():
    # Caso de prueba 1
    resultado = Tarefa7.obtener_info_nombre("Manuel")
    assert resultado == ("MANUEL", 6)  # Ajustado para reflejar la longitud correcta de la cadena

    # Caso de prueba 2
    resultado = Tarefa7.obtener_info_nombre("Juan")
    assert resultado == ("JUAN", 4)