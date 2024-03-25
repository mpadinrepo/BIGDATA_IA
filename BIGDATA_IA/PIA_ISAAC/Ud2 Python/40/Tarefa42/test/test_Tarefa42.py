# test_Tarefa42.py

from Tarefa42 import aplicar_iva_21, aplicar_iva_04, aplicar_descuento, calcular_total_cesta

def test_aplicar_iva_21():
    assert aplicar_iva_21(100) == 21.0
    assert aplicar_iva_21(50) == 10.5
    assert aplicar_iva_21(0) == 0

def test_aplicar_iva_04():
    assert aplicar_iva_04(100) == 4.0
    assert aplicar_iva_04(75) == 3.0
    assert aplicar_iva_04(0) == 0

def test_aplicar_descuento():
    assert aplicar_descuento(100, 10) == 90.0
    assert aplicar_descuento(50, 5) == 47.5
    assert aplicar_descuento(0, 20) == 0

def test_calcular_total_cesta():
    cesta = [
        {'prezo_sin_iva': 100, 'funcion_descuento': aplicar_descuento, 'funcion_iva': aplicar_iva_21},
        {'prezo_sin_iva': 75, 'funcion_descuento': aplicar_descuento, 'funcion_iva': aplicar_iva_04},
        {'prezo_sin_iva': 50, 'funcion_descuento': aplicar_descuento, 'funcion_iva': aplicar_iva_21},
    ]
    total, iva, descuento = calcular_total_cesta(cesta, porcentaje_descuento=4)  # Asegúrate de pasar el porcentaje_descuento
    assert total == 210.0
    assert iva == 34.5
    assert descuento == 35.0