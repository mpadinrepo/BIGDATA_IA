""" Tarefa 5
Escribir un programa que pregunte ao usuario polo número de horas traballadas
e o custo por hora. 
Despois debe mostrar por pantalla a paga que lle corresponde. """
""" 
numerodehoras = int(input("Por favor ingrese el numero de horas trabajadas: "))
custeporhoras = int(input("Por favor ingrese el coste de hora trabajada: "))
                    
paga = numerodehoras * custeporhoras
print ("se ha indicado que se ha trabajado",numerodehoras,"horas, y siendo el coste por hora: ",custeporhoras,"€/hora")
print("el calculo resultado total: ",paga,"€")

 """

def mostrar_mensaje(mensaje):
    print("*************************************************")
    print(mensaje)
    print("*************************************************")

def carga_suma():
    numerodehoras=int(input("Ingrese las horas trabajadas: "))
    custeporhoras=int(input("Ingrese el coste por hora trabajada: "))
    suma=numerodehoras*custeporhoras
    print("La suma de los dos valores es:",suma)


# programa principal

mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado.")
carga_suma()
mostrar_mensaje("Gracias por utilizar este programa")