def calcular_ive_21(cantidad):
    return cantidad * 0.21

def calcular_ive_4(cantidad):
    return cantidad * 0.04

def aplicar_descuento_10(cantidad):
    return cantidad * 0.10

def calcular_total_compra(cesta):
    total_pagar = 0
    iva_total = 0
    descuento_total = 0

    for producto in cesta:
        precio_sin_ive = producto['precio_sin_ive']
        calcular_ive = producto['calcular_ive']
        aplicar_descuento = producto['aplicar_descuento']

        iva_total += calcular_ive(precio_sin_ive)

        if aplicar_descuento:
            descuento_total += aplicar_descuento(precio_sin_ive)

        total_pagar += precio_sin_ive + calcular_ive(precio_sin_ive) - descuento_total

    return total_pagar, iva_total, descuento_total

# Ejemplo de uso:
lista_compra = [
    {'precio_sin_ive': 100, 'calcular_ive': calcular_ive_21, 'aplicar_descuento': aplicar_descuento_10},
    {'precio_sin_ive': 50, 'calcular_ive': calcular_ive_4, 'aplicar_descuento': None},
    # Agrega más productos a la lista según sea necesario
]

total, iva, descuento = calcular_total_compra(lista_compra)

print(f'Total a pagar: {total}€')
print(f'IVA: {iva}€')
print(f'Descuento aplicado: {descuento}€')
