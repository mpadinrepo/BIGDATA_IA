#hacer un programa que tome por teclado dos numeros y si num1 es mayor que num2 sumar los valores
#si num no es mayor que num2 entonces que muestre el producto y la division de los valores.

num1 = int(input("Introduzca el primer valor: "))
num2 = int(input("Introduzca el segundo valor: "))



if num1 > num2:
    suma = num1 + num2
    diferencia = num1 - num2
    print ("la suma de los dos valores es:")
    print (suma)
    print ("la diferencia de los valores es:")
    print (diferencia)
else:
    producto = num1 * num2
    division = num1 / num2
    print ("el producto de los valores es_")
    print(producto)
    print("la division de los valores es: ")
    print (division)