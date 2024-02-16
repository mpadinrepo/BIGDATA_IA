""" Tarefa 6
Escribir un programa que pregunte o nome completo do usuario na consola
e despois mostre por pantalla o nome completo do usuario tres veces,
unha con todas as letras minúsculas
outra con todas as letras maiúsculas
e outra só coa primeira letra do nome e dos apelidos en maiúscula. 
O usuario pode introducir o seu nome combinando maiúsculas e minúsculas como queira. """




def recogerdatos():
    nombres = input("Por favor escriba su nombre: ")
    apellidos = input("Por favor escriba sus apellidos: ")
    nombrecompleto = nombres + " " + apellidos
    return nombrecompleto

# Llamamos a la función y almacenamos el resultado en una variable
nombre_completo = recogerdatos()



#outputs

print("Su nombre completo es:", nombre_completo)
print(nombre_completo+" " + nombre_completo +" " + nombre_completo)
print("Su nombre completo en minusculas:", nombre_completo.lower())
print("Su nombre completo en mayusculas:", nombre_completo.upper())
print("Su nombre completo en Title:", nombre_completo.title())
print("Su nombre completo en Capitalize:", nombre_completo.capitalize())
print("Su nombre completo invertido:", nombre_completo.swapcase())