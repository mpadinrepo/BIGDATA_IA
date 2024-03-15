def aplicar_funcion_a_lista(lista, funcion):
    """
    Aplica una función dada a cada elemento de la lista y devuelve una nueva lista.

    Parameters:
    - lista (list): La lista de entrada.
    - funcion (callable): La función a aplicar a cada elemento de la lista.

    Returns:
    - list: Una nueva lista donde cada elemento es el resultado de aplicar la función al elemento original.
    """
    return [funcion(elemento) for elemento in lista]

# Test unitarios
def test_aplicar_funcion_a_lista():
    # Test con una función que duplica el elemento
    assert aplicar_funcion_a_lista([1, 2, 3], lambda x: x * 2) == [2, 4, 6]

    # Test con una función que eleva al cuadrado
    assert aplicar_funcion_a_lista([2, 4, 6], lambda x: x ** 2) == [4, 16, 36]

    # Test con una función que devuelve el mismo elemento
    assert aplicar_funcion_a_lista([10, 20, 30], lambda x: x) == [10, 20, 30]

    # Test con una función que agrega una cadena al final
    assert aplicar_funcion_a_lista(["a", "b", "c"], lambda x: x + "_final") == ["a_final", "b_final", "c_final"]

    print("Todos los tests pasaron con éxito.")

# Ejecutar los test unitarios
test_aplicar_funcion_a_lista()
