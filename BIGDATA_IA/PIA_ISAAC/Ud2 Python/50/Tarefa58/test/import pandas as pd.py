import pandas as pd
import numpy as np

# Ruta del archivo
ruta_archivo = "/media/DIURNO/CURSO/PIA_ISAAC/Ud2 Python/TarefazPIA/Tarefa58/iris.data"

# Cargar datos utilizando Pandas
datos_pd = pd.read_csv(ruta_archivo, header=None, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class'])

# Normalizar la primera columna (sepallength)
sepallength_normalizado_array = (datos_pd['sepallength'] - datos_pd['sepallength'].min()) / (datos_pd['sepallength'].max() - datos_pd['sepallength'].min())

# Obtener las primeras filas del DataFrame
head_pd = datos_pd.head()

# Imprimir resultados
print("Primeras filas del DataFrame:")
print(head_pd)

print("\nColumna sepallength normalizada como array:")
print(sepallength_normalizado_array.values)