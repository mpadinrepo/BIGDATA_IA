#se ingresa por teclado un numero positivo de uno o dos digitos 1...99 ,
#mostrar un mensaje indicando si el numero tiene uno o dos digitos.
#hay que tener en cuenta la condición debe cumplirse para tener dos digitos un numero entero

numeroenteropositivo = int( input ("Ingrese por teclado un numero entero positivo de 1 o 2 digitos: "))

if numeroenteropositivo >= 10:
    print(numeroenteropositivo,"Tiene dos digitos")
else:
    print(numeroenteropositivo,"Tiene un digito")