""" Se ingresan tres valores por teclado, 
si todos son iguales se imprime la suma del primero con el segundo
y a este resultado se lo multiplica por el tercero. """


num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))
print("los valores ingresados son: ",num1,num2,num3)

if num1 == num2 and num1 == num3:
    sumar = num1+num2
    multiplicacion = sumar * num3
    print("calculo1 suma: ",sumar)
    print("calculo2 multiplicacion: ",multiplicacion)
else:
    print ("retry")