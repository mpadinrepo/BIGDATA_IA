""" Tarefa 6

Escribir un programa que pregunte o nome completo do usuario na consola
e despois mostre por pantalla o nome completo do usuario tres veces
1)unha con todas as letras minúsculas
2)outra con todas as letras maiúsculas
3)outra só coa primeira letra do nome e dos apelidos en maiúscula. 

O usuario pode introducir o seu nome combinando maiúsculas e minúsculas como queira. """

nombre= str(input ("Digame su nombre: "))
apellido1 = str(input ("Digame su primer apellido: "))
apellido2 = str(input ("Digame su segundo apellido: "))

nombrelower= str(nombre.lower())
nombreupper= str(nombre.upper())
nombrecapitalize= str(nombre.capitalize())

apellido1lower= str(apellido1.lower())
apellido2lower=str(apellido2.lower())
apellido1upper= str(apellido1.upper())
apellido2upper= str(apellido2.upper())
apellido1capitalize= str(apellido1.capitalize())
apellido2capitalize=str(apellido2.capitalize())


print (nombreupper,apellido1upper,apellido2upper)
print (nombrelower,apellido1lower,apellido2lower)
print (nombrecapitalize,apellido1capitalize,apellido2capitalize)
