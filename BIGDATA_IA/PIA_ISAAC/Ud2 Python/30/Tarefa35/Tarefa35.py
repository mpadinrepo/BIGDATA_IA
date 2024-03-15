# Tarefa 35

# Escribir un programa que almacene as materias dun curso nunha lista, (por exemplo Matemáticas, Física, Química, Historia e Lingua) 
materias=['Matematicas','Fisica','Quimica','Historia','Lengua']
notas={}
# pregunte ao usuario a nota que sacou en cada materia e elimine da lista as materias aprobadas. 


for materia in materias:
    nota = float(input (f'Ingrese la nota que sacó en la materia de: {materia}: '))
    notas[materia]=nota
aprobados = [materia for materia, nota in notas.items() if nota >= 5]


for aprobados in aprobados:
    materias.remove(aprobados)
# Ao final o programa debe mostrar por pantalla as materias que o usuario ten que repetir.
if len(materias) > 0:
    print("\nDebes repetir las siguientes materias:")
    for materia in materias:
        print(materia)
else:
    print("\n¡Felicidades! Has aprobado todas las materias.")