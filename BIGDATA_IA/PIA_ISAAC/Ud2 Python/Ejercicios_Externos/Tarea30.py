""" Problema 3:
Desarrollar un programa que permita la carga de 10 valores por teclado
y nos muestre posteriormente la suma de los valores ingresados y su promedio. """

# num1 = int (input("Ingrese el valor num1: "))
# num2 = int (input("Ingrese el valor num2: "))
# num3 = int (input("Ingrese el valor num3: "))
# num4 = int (input("Ingrese el valor num4: "))
# num5 = int (input("Ingrese el valor num5: "))
# num6 = int (input("Ingrese el valor num6: "))
# num7 = int (input("Ingrese el valor num7: "))
# num8 = int (input("Ingrese el valor num8: "))
# num9 = int (input("Ingrese el valor num9: "))
# num10 = int (input("Ingrese el valor num10: "))

# suma = num1+num2+num3+num4+num5+num6+num7+num8+num9+num10
# promedio = suma/10
# print("Suma: ",suma)
# print("Promedio: ",promedio)


#---> con while

x = 1
suma = 0
while x <= 10:
    valor = int(input("Ingrese un valor: "))
    suma = suma + valor
    x = x + 1
promedio = suma//10
#promedio = suma/10 con decimales
print("suma: ",suma)
print("promedio: ",promedio)