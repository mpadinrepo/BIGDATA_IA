#1 Obtén los elementos que se encuentran en a y en b en la misma posición:
import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

elementos_en_la_misma_posicion = a[a == b]

print("elementos que se encuentran en a y en b en la misma posición:",elementos_en_la_misma_posicion)

#2 Obtén todos los números del array a que se encuentren entre 5 y 10:
import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])

numeros_entre_5_y_10 = a[(a >= 5) & (a <= 10)]

print("números del array a que se encuentren entre 5 y 10: ",numeros_entre_5_y_10)

#3 Define la función maxx y aplícala de manera vectorial a los arrays a y b:
######################################
import numpy as np

def maxx(x, y):
    """Obtener el máximo de dos elementos"""
    return np.maximum(x, y)

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

resultado = maxx(a, b)

print("Define la función maxx y aplícala de manera vectorial a los arrays a y b: ",resultado)

######################################
""" 4. Lee mediante pandas o ficheiro iris.data. Obten a columna sepallength como un array numpy. Normaliza os datos: os novos valores terán un valor minimo de 0 e maximo de 1.
Podes descargar os ficheiros de datos de aquí: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/
Nesa url tes tanto o ficheiro de datos como a súa descrición. """


import pandas as pd

# Ruta del archivo iris.data
ruta_archivo = "/media/DIURNO/CURSO/PIA_ISAAC/Ud2 Python/TarefazPIA/Tarefa58/iris.data"
# Nombres de las columnas
nombres_columnas = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class']
# Cargar el archivo iris.data usando pandas
datos_iris = pd.read_csv(ruta_archivo, header=None, names=nombres_columnas)
# Obtener la columna 'sepallength' como un array numpy
sepallength_array = datos_iris['sepallength'].values
# Normalizar los datos para que estén entre 0 y 1
sepallength_normalizado = (sepallength_array - sepallength_array.min()) / (sepallength_array.max() - sepallength_array.min())
# Imprimir los valores normalizados por pantalla
print(sepallength_normalizado)