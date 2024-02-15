""" Se ingresan por teclado tres números,
si todos los valores ingresados son menores a 10 imprimir en pantalla la leyenda 
"Todos los números son menores a diez". """

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))
print("los valores ingresados son: ")
if num1<10 and num2<10 and num3<10:
    print("Todos los valores ingresados son menores de 10")
else:
    print("Hay valores ingresados superiores a 10")