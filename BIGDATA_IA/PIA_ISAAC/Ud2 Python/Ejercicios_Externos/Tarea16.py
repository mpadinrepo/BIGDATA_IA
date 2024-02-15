# se ingresa por teclado un valor entero,mostrar una leyenda que indique
#si el numer es positivo,negativo o nulo (es decir ZERO)

numero = int(input=("Ingrese por teclado un valor entero: "))

if numero == 0:
    print ("el valor introducido es nulo")
else:
    if numero > 0:
        print ("el numero es positivo")
    else:
        print("el numero es negativo")