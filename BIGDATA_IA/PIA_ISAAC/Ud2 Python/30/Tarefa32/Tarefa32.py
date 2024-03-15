""" Tarefa 32
z
Escribir un programa que almacene as materias dun curso
(por exemplo Matemáticas, Física, Química, Historia e Lingua)
nunha lista, pregunte ao usuario a nota que sacou en cada materia,
e despois as amose por pantalla coa mensaxe En <materia> sacaches
un <nota> onde <materia> é cada unha das materias da lista e
<nota> cada unha das correspondentes notas introducidas polo usuario. """

# materias=[]
# notas=[]
# def registrar_notas (materias,notas):
#      materias = []

#      de aplicares a función ao elemento orixinal da lista.'''
# def recolector (lista,funcion):
    
#     lista = (1,2,3,4,5,6,7,8,9,0)
#     funcion lista (*)
    
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for materia in materias:
    notas.append(input(f"Ingrese la nota que sacó en {materia}: "))

for i in range(len(materias)):
    print(f"En {materias[i]} sacaste un {notas[i]}, donde {materias[i]}")