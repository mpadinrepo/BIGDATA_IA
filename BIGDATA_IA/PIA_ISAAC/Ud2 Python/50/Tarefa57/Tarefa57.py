""" Tarefa 57 - Numpy
1. Crea un array de 1D cos números do 0 ao 9
2. Crea un array de 1D cos números do 1 ao 10
3. Indica dos elementos do seguinte array cales son pares:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
4. Do seguinte array, substitúe todos os números impares por 0
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
5. Une os arrays a e b de xeito que as filas de b se encontren debaixo das de a.
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
6. Une os arrays a e b de xeito que as columnas de b se encontren a dereita das de a.
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
"""
#1. 
import numpy as np
array1d = np.arange(10)
print("1:Crea un array de 1D cos números do 0 ao 9", array1d)

#2.
import numpy as np
array1d = np.arange(1, 11)
print("2:Crea un array de 1D cos números do 1 ao 10", array1d)

#3. 
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arraypares = arr[arr % 2 == 0]
print("3:Indica dos elementos do seguinte array cales son pares:", arraypares)

#4.
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Substituir todos os números ímpares por 0
arr[arr % 2 != 0] = 0
print("4:Array después de substituir impares por 0:", arr)

#5.
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
arraysuma = np.vstack((a, b))
print("5:Une os arrays a e b de xeito que as filas de b se encontren debaixo das de a.", arraysuma)

#6.
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
resultado_concatenate = np.concatenate((a, b), axis=1)
print("6:Une os arrays a e b de xeito que as columnas de b se encontren a dereita das de a.")
print(resultado_concatenate)