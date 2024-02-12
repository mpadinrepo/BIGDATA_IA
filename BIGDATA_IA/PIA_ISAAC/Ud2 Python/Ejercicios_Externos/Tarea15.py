#se carga por pantalla 3 numeros y muestra por pantalla el mayor de ellos
num1 = int (input("Ingrese el primer valor: "))
num2 = int (input("Ingrese el segundo valor: "))
num3 = int (input("Ingrese el tercer valor: "))

print ("El valor mayor introducido es es: ")
if num1 > num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)