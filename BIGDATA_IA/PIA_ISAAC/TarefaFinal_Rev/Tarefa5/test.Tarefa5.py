# test_Tarefa5

# Importa la función que calcula la paga desde el archivo de programa
from Tarefa5 import numerodehoras, custoporhora

def test_calcular_paga():
    numerodehoras = 40
    custoporhora = 10
    resultado_esperado = 400
    assert numerodehoras * custoporhora == resultado_esperado

    numerodehoras = 0
    custoporhora = 10
    resultado_esperado = 0
    assert numerodehoras * custoporhora == resultado_esperado

    numerodehoras = 45
    custoporhora = 12
    resultado_esperado = 540
    assert numerodehoras * custoporhora == resultado_esperado
