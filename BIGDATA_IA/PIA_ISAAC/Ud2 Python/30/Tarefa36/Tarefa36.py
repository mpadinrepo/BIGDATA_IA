""" Escribir un programa que garde nunha variable o dicionario
{'Euro':'€', ' Dollar':'$', ' Yen':'¥'}, 
pregunte ao usuario por unha divisa e mostre
o seu símbolo ou unha mensaxe de aviso se a divisa
non está no dicionario. """

#Diccionario DIVISAS
diccionario_divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥','Libra':'£ '}

# Pregunta al usuario por una divisa
# Busca la divisa en el diccionario
# Muestra el símbolo o un mensaje de aviso
recolector_divisas = input("Introduce una divisa: ")
simbolo = diccionario_divisas.get(recolector_divisas)

if simbolo:
    print(f"El simbolo de {recolector_divisas} es: {simbolo}")
else:
    print(f"¡La divisa {recolector_divisas} no tenemos la divisa en el diccionario!")