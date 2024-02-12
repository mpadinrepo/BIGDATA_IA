# Se ingresan 3 notas de un alumno, si el promedio es mayor o igual a 7
#mostrar un mensaje "Promocionado"
 
nota1 = int(input("Por favor la primera nota: "))
nota2 = int(input("Por favor la segunda nota: "))
nota3 = int(input("Por favor la tercera nota: "))
sumanotas = nota1+nota2+nota3
promedio = sumanotas/3

if promedio >= 7:
    print ("PROMOCIONADO")
else:
    print ("NO PROMOCIONADO")   