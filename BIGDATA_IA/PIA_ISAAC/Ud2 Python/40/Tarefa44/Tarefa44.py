def es_primo(numero):
    """
    Verifica si un número dado es primo.

    Parameters:
    - numero (int): El número a verificar.

    Returns:
    - bool: True si el número es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_en_lista(lista):
    """
    Encuentra los números primos en una lista dada.

    Parameters:
    - lista (list): La lista de números.

    Returns:
    - list: Una lista con los números primos de la lista original.
    """
    return [numero for numero in lista if es_primo(numero)]

# Test unitario
def test_numeros_primos_en_lista():
    assert numeros_primos_en_lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7]
    assert numeros_primos_en_lista([11, 13, 17, 19, 23]) == [11, 13, 17, 19, 23]
    assert numeros_primos_en_lista([4, 6, 8, 9, 10]) == []
    assert numeros_primos_en_lista([]) == []

    print("Todos los tests pasaron con éxito.")

# Ejecutar los test unitarios
test_numeros_primos_en_lista()
