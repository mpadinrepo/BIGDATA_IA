# Tarefa 5

# Escribir un programa que pregunte ao usuario polo número de horas traballadas e o custo por hora. 
#Despois debe mostrar por pantalla a paga que lle corresponde.


""" sin funcion

numerodehoras = int(input ("Escriba el numero de horas trabajadas: "))
custoporhora = int(input ("Escriba el custo por hora: "))

resultado = numerodehoras * custoporhora
print(f"el resultado de Horas trabajads por custo por hora hace un total de: ", resultado ) """

# con funcion

def calcular_paga(numerodehoras, custoporhora):
    resultado = numerodehoras * custoporhora
    return resultado
numerodehoras = int(input ("Escriba el numero de horas trabajadas: "))
custoporhora = int(input ("Escriba el custo por hora: "))

resultado = calcular_paga(numerodehoras, custoporhora)
print(f"El resultado de Horas trabajadas por costo por hora hace un total de: {resultado}")
