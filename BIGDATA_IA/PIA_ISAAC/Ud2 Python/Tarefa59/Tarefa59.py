""" Tarefa 59 - Numpy

1. Lee mediante pandas o ficheiro iris.data. Obtén un lista cos valores únicos da columna class

2. Lee mediante pandas o ficheiro iris.data. Obtén un lista cos valores únicos da columna class e asignalles a cada un deles un valor numérico de xeito automático. Crea unha nova columna onde se cambie o valor categórico polo número.

3. Lee mediante pandas o ficheiro iris.data. Obtén un lista cos valores únicos da columna class. Crea unha nova columna por cada categoría, na que aparecerá un 1 se a fila pertence a esa clase. """



import pandas as pd

# Ruta del archivo iris.data
ruta_archivo = "/media/DIURNO/CURSO/PIA_ISAAC/Ud2 Python/TarefazPIA/Tarefa58/iris.data"
# Nombres de las columnas
nombres_columnas = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class']
# Cargar el archivo iris.data usando pandas
datos_iris = pd.read_csv(ruta_archivo, header=None, names=nombres_columnas)
print(f"1 - Obtén un lista cos valores únicos da columna class: ",datos_iris)


valores_unicos_class = datos_iris['class'].unique()

print(f"valores unicos: ",valores_unicos_class)





import pandas as pd

# Ruta del archivo iris.data
ruta_archivo = "/media/DIURNO/CURSO/PIA_ISAAC/Ud2 Python/TarefazPIA/Tarefa58/iris.data"
# Nombres de las columnas
nombres_columnas = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class']
# Cargar el archivo iris.data usando pandas
datos_iris = pd.read_csv(ruta_archivo, header=None, names=nombres_columnas)

# Obtener valores únicos de la columna 'class'
valores_unicos_class = datos_iris['class'].unique()

# Asignar valores numéricos de manera automática
dict_mapping = {valor: index for index, valor in enumerate(valores_unicos_class)}

# Crear nueva columna con valores numéricos
datos_iris['class_numerico'] = datos_iris['class'].map(dict_mapping)

print(datos_iris)




import pandas as pd

# Ruta del archivo iris.data
ruta_archivo = "/media/DIURNO/CURSO/PIA_ISAAC/Ud2 Python/TarefazPIA/Tarefa58/iris.data"
# Nombres de las columnas
nombres_columnas = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class']

# Cargar el archivo iris.data usando pandas
datos_iris = pd.read_csv(ruta_archivo, header=None, names=nombres_columnas)

# Obtener valores únicos de la columna 'class'
valores_unicos_class = datos_iris['class'].unique()

# Crear nuevas columnas por cada categoría
for valor in valores_unicos_class:
    datos_iris[valor] = (datos_iris['class'] == valor).astype(int)

print(f"con columna nueva: ",datos_iris)
