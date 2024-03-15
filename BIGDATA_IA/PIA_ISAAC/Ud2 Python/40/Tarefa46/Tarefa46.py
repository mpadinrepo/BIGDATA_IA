def calcular_precio_inmueble(inmueble):
    """
    Calcula el precio de un inmueble en función de su zona.

    Parameters:
    - inmueble (dict): Diccionario que representa un inmueble con sus atributos.

    Returns:
    - float: Precio calculado del inmueble.
    """
    metros = inmueble['metros']
    habitaciones = inmueble['habitacións']
    garaje = inmueble['garaxe']
    antiguedad = 2024 - inmueble['ano']  # Se asume el año actual como 2024

    if inmueble['zona'] == 'A':
        precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100)
    elif inmueble['zona'] == 'B':
        precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100) * 1.5
    else:
        precio = 0  # Zona no válida, asignamos 0 al precio

    return precio

def buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto):
    """
    Busca inmuebles en función de un presupuesto dado.

    Parameters:
    - lista_inmuebles (list): Lista de inmuebles representados como diccionarios.
    - presupuesto (float): Presupuesto máximo para la búsqueda.

    Returns:
    - list: Lista de inmuebles que cumplen con el presupuesto, con un nuevo atributo 'prezo'.
    """
    inmuebles_cumplen_presupuesto = []

    for inmueble in lista_inmuebles:
        precio = calcular_precio_inmueble(inmueble)
        inmueble_con_precio = inmueble.copy()
        inmueble_con_precio['prezo'] = precio

        if precio <= presupuesto:
            inmuebles_cumplen_presupuesto.append(inmueble_con_precio)

    return inmuebles_cumplen_presupuesto

# Ejemplo de uso:
lista_inmuebles = [
    {'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe': True, 'zona': 'A'},
    {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe': True, 'zona': 'B'},
    {'ano': 1980, 'metros': 120, 'habitacións': 4, 'garaxe': False, 'zona': 'A'},
    {'ano': 2005, 'metros': 75, 'habitacións': 3, 'garaxe': True, 'zona': 'B'},
    {'ano': 2015, 'metros': 90, 'habitacións': 2, 'garaxe': False, 'zona': 'A'}
]

presupuesto_usuario = float(input("Introduce tu presupuesto: "))

inmuebles_cumplen_presupuesto = buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto_usuario)

# Imprime los inmuebles que cumplen con el presupuesto
print("Inmuebles que cumplen con el presupuesto:")
for inmueble in inmuebles_cumplen_presupuesto:
    print(inmueble)
