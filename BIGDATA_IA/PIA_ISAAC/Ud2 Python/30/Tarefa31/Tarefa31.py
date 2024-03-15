# Tarefa 31

# Escribir un programa que almacene as materias dun curso 
# (por exemplo Matemáticas, Física, Química, Historia e Lingua)
# nunha lista e a mostre por pantalla coa mensaxe
# !"Eu estudo <materia>, onde <materia> é cada unha das materias da lista."

# listaasignaturas = []

# numerode = int(input("Ingrese elementos: "))


# for _ in range(cantidad_elementos):
#     elemento = input("Ingrese un elemento: ")
#     listaasignaturas.append(elemento)

# print("La lista creada es:", listaasignaturas)
# Tarefa 31


lista_asignaturas = []

cantidad_elementos = int(input("Ingrese el número de asignaturas a registrar: "))


for _ in range(cantidad_elementos):
    materia = input("Ingrese una materia: ")
    lista_asignaturas.append(materia)

for materia in lista_asignaturas:
    print("Yo estudio", materia)