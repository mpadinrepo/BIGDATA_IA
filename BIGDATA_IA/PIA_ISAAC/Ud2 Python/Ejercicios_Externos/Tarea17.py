""" confeccionar un programa que permita cargar un numero entero positivo
hasta tres cifras y muestre un mensaje indicnado si tiene 1,2 o 3 cifras, 
mostrar un mensaje de error si el numero de cifras es mayor
 """

numero = int(input("Ingrese un numero del 0 al 999: "))

if numero < 10:
    print ("Tiene un digito")
else:
    if numero < 100:
        print ("Tiene dos digitos")
    else:
        if numero < 1000:
            print ("Tiene tres digitos")
        else:
            print("ERROR, numero introducido mayor a 3 digitos")
print ("FIN DEL PROGRAMA")