""" Tarefa 33

Escribir un programa que pregunte ao usuario os números gañadores da lotería primitiva,
os almacene nunha lista e logo os amose por pantalla ordenados de menor a maior.
########################3
cantidad= int(input ('Por favor cuantos numeros de loteria va a grabar? :'))
lista_numeros_loteria=[]
for _ in range(cantidad):
    numeros_de_loteria = int(input("Ingrese numero loteria: "))
    lista_numeros_loteria.append(lista_numeros_loteria)
print (lista_numeros_loteria[:])
"""
cantidad = int(input('Cuantos decimos vas a ingresar? :'))

lista_numeros_loteria = []

for decimos in range(cantidad):
    numero_de_loteria = int(input("Ingrese numero de loteria: "))
    lista_numeros_loteria.append(numero_de_loteria)

lista_numeros_loteria.sort()

print(f"Números de lotería ordenados de menor a mayor:", lista_numeros_loteria)