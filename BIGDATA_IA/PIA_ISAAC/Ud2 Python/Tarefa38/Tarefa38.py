""" Tarefa 38

Escribir un programa que garde nun dicionario os prezos das froitas da táboa,
pregunte ao usuario por 
* unha froita
* un número de quilos

e mostre por pantalla o prezo dese número de quilos de froita. 

Se a froita non está no dicionario debe mostrar unha mensaxe informando diso.
"""
# Dicionario de prezos das froitas
diccionario_precios = {
    'platano': 1.35,
    'manzana': 0.80,
    'pera': 0.85,
    'naranja': 0.70
}

# solicitamos input de nombre de fruta
fruta = input("que fruta quieres? ").lower()  
# Convierte la entrada a minúsculas para evitar problemas de mayúsculas/minúsculas


kilos = float(input("Cuantos kilos?: "))

# Comprobar se a froita está no dicionario
if fruta in diccionario_precios:
# Calcular precio
    precio_total = diccionario_precios[fruta] * kilos
# Mostrar precio
    print(f"el Precio de {kilos} Kgs de {fruta} es: {precio_total} euros")
else:
# Error si no existe la fruta que ingresan
    print(f"la fruta que indicas : {fruta} no está disponible.")
