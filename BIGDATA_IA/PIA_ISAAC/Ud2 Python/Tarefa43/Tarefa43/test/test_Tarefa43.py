import unittest
from Tarefa43 import aplicar_funcion_a_lista, calcular_cuadrado, calcular_cubo
# ... Resto del código de tu archivo de prueba ...

def calcular_cuadrado_prueba(numero):
    return numero ** 2

def calcular_cubo_prueba(numero):
    return numero ** 3

class TestAplicarFuncionALista(unittest.TestCase):
    def test_calcular_cuadrado(self):
        numeros = [1, 2, 3, 4, 5]
        resultado_esperado = [1, 4, 9, 16, 25]
        self.assertEqual(aplicar_funcion_a_lista(numeros, calcular_cuadrado_prueba), resultado_esperado)

    def test_calcular_cubo(self):
        numeros = [1, 2, 3, 4, 5]
        resultado_esperado = [1, 8, 27, 64, 125]
        self.assertEqual(aplicar_funcion_a_lista(numeros, calcular_cubo_prueba), resultado_esperado)

if __name__ == '__main__':
    unittest.main()
