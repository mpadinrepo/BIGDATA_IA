""" Escribir un programa que pregunte o nome do usuario na consola e despois de que o usuario introdúzao
mostre por pantalla <usuario> ten < n> letras,
onde  é o nome de usuario en maiúsculas e < n> é o número de letras que teñen o nome. """


# nombrecompleto= str(input ("Digame su nombre: "))

# nombreupper= str(nombrecompleto.upper())
# caracteres=len(nombrecompleto)
# print ("El nombre en mayusculas es :", nombreupper)
# print ((len(nombrecompleto)),"es el numero de letras que tiene el nombre")

# programa.py

# Tarefa7.py

def obtener_info_nombre(nombrecompleto):
    nombreupper = nombrecompleto.upper()
    caracteres = len(nombrecompleto)
    return nombreupper, caracteres