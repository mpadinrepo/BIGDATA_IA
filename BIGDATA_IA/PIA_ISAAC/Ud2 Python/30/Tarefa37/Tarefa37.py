"""     Tarefa 37

Escribir un programa que pregunte ao usuario o seu:
nome, idade, dirección e teléfono e o garde nun dicionario. 
Despois debe mostrar por pantalla a mensaxe
ten x anos, vive en <dir> e o seu número de teléfono é <num>. """
#se crea diccionario vacio
usuario = {}
#recopilar datos del usuario
nombre=str(input ("Escriba su nombre: "))
edad=str(input ("Escriba cuantos años tienes: "))
direccion=str(input ("Escriba la dirección: "))
telefono= str (input ("Escriba su numero de telefono:"))
#Grabar datos en variables 
usuario['nombre']= nombre
usuario['edad'] = edad
usuario['direccion'] = direccion
usuario['telefono'] = telefono
#retornar información concatenadas las strings
informacion_usuario = "el usuario " + usuario['nombre'] + " tiene " + usuario['edad'] + " años, vive en " + usuario['direccion'] + " y su número de teléfono es " + usuario['telefono'] + "."
#imprimir la informacion
print(informacion_usuario)