def son_todos_pares(lista):
    """
    Verifica si todos los elementos de una lista son pares.

    Parameters:
    - lista (list): La lista de números.

    Returns:
    - bool: True si todos los elementos son pares, False en caso contrario.
    """
    return all(numero % 2 == 0 for numero in lista)

# Ejemplo de uso:
lista_ejemplo = [2, 4, 6, 8, 10, 11]
resultado = son_todos_pares(lista_ejemplo)

if resultado:
    print("Todos los elementos de la lista son pares.")
else:
    print("Al menos uno de los elementos de la lista no es par.")
