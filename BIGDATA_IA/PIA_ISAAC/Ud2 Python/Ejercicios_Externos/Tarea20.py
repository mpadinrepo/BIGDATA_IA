""" Problema:
Se carga una fecha (día, mes y año) por teclado. 
Mostrar un mensaje si corresponde al primer trimestre del año (enero, febrero o marzo)
Cargar por teclado el valor numérico del día, mes y año.
Ejemplo: dia:10 mes:2 año:2018 """

# dia = int(input("Ingrese el dato 'dia'"))       
# mes = int(input("Ingrese el dato 'mes'"))
# año= int(input("Ingrese el dato 'año'"))
# print("la fecha introducida es :" ,dia,mes,año)
# print("la fecha corresponde al: ")
# if mes <= 3:
#     print("primer trimestre")
# else:
#     if mes <=6:
#         print("segundo semestre")
#     else:
#         if mes <=9:
#             print("tercer trimestre")
#         else:
#             print("cuarto trimestre")
# print("Fin de programa")

dia = int(input("Ingrese el dato 'dia'"))       
mes = int(input("Ingrese el dato 'mes'"))
año= int(input("Ingrese el dato 'año'"))
print("la fecha introducida es :" ,dia,mes,año)
print("la fecha corresponde al: ")

if mes == 1 or mes == 2 or mes == 3:
    print ("Primer Trimestre")
else:
    print ("no corresponde al primer trimestre")