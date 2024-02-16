"""Tarefa 8
Os teléfonos dunha empresa teñen o seguinte formato
prefixo-número-extension
onde o prefixo é o código do país +34, e a extensión ten dous díxitos 
(por exemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato
e mostre por pantalla o número de teléfono sen o prefixo e a extensión."""


""" 
numero = str(input( "introduzca su numero de telefono: "))
extension = str(input ("Introduzca su extension: "))
prefixo = "+34"
numerocompleto = prefixo + "-" + numero + "-" + extension
print (numerocompleto)
"""  """

def componernumero (prefixo:"+34",numero,extension):
    numero = str(input( "introduzca su numero de telefono: "))
    extension = str(input ("Introduzca su extension: "))
    return numerocompleto
print (numerocompleto)
 """

def mostrar_mensaje(mensaje):
    print ("**************************************")
    print (mensaje)
    print ("**************************************")
###############################################
def carga_numero():
    prefixo = "+34"
    numero = input("Ingrese el numero de telefono: ")
    extension = input("Ingrese el numero de extensión: ")
    if len(extension) != 2:
        print("El dato de extensión debe tener exactamente 2 caracteres.")
        return  # Detiene la ejecución de la función si la longitud de la extensión no es 2
    numerocompleto = f"{prefixo}-{numero}-{extension}"
    print("El numero de telefono con formato adaptado es:", numerocompleto)

# Mostrar mensaje inicial
mostrar_mensaje("Bienvenido a mi PROGRAMA, su funcion es cambiar al formato adecuado numeros de telefono (por exemplo +34-913724710-56).")

# Ejecutar la carga de número
carga_numero()

# Mostrar mensaje de agradecimiento
mostrar_mensaje("Gracias por usar mi programa")
