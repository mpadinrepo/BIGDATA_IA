""" Escribir un programa que solicite ingresar 10 notas de alumnos
y nos informe cuántos tienen notas mayores o iguales a 7
y cuántos menores """

x = 1
mayor=0
menor=0
while x <= 10:
    nota = int(input ("Ingrese las 10 notas a procesar: "))
    if nota >= 7:
        mayor = mayor + 1
    else:
        menor = menor + 1
    x = x + 1
print("numero de notas Mayor a 7: ",mayor)
print ("numero de notas Menores a 7: ",menor)
