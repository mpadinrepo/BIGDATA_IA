""" Se ingresan un conjunto de n alturas de personas por teclado.
Mostrar la altura promedio de las personas. """


x=1
n= int(input ="Cuantas personas vas a procesar:")
suma=0
while x <= n:
    altura = input = int(print="Ingrese el valor de altura: ")
    suma = suma + altura
    x = x + 1
promedio = suma
print("este es el promedio",promedio)