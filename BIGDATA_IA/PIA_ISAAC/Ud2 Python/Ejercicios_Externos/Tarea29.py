""" Codificar un programa que solicite la carga de un valor positivo
y nos muestre desde 1 hasta el valor ingresado de uno en uno.

Ejemplo: Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 30. """


n = int(input("Ingrese el valor: "))
print ("INICIO DE PROGRAMA")
x=1
while x <= n:
    print(x)
    x= x + 1

print ("FIN DE PROGRAMA")