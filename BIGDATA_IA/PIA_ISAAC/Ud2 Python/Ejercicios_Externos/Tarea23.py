""" Se ingresan por teclado tres números, 
si al menos uno de los valores ingresados es menor a 10,
imprimir en pantalla la leyenda
"Alguno de los números es menor a diez". """

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))
print("los valores ingresados son: ")

if num1<10 or num2<10 or num3<10:
    print("Alguno de los valores es menor de diez")
else:
    print ("todos los numeros son mayores de diez")
