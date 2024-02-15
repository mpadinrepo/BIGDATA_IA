""" Problemas propuestos
Realizar un programa que pida cargar una fecha cualquiera,
luego verificar si dicha fecha corresponde a Navidad """

DiaNavidad=25
MesNavidad=12
Navidad = DiaNavidad, MesNavidad

dia = int (input ("Ingrese el dia por teclado: "))
mes = int (input ("Ingrese el mes por teclado: "))
anho= int (input ("Ingrese el año por teclado: "))
print("La fecha introducida: ")
if dia == DiaNavidad and mes == MesNavidad:
    print ("Es Navidad")
else:
    print("No es Navidad")
print("Fin de programa")                                                                                                                                                                                            