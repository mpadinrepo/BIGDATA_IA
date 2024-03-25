# Escribir un programa que almacene nunha lista os números do 1 ao 10
numeros = list(range(1, 11))

numeros_invertidos = list(reversed(numeros))
numeros_string = [str(num) for num in numeros_invertidos]


# Usa o metodo join da clase string para separalos por comas
numeros_separados_por_comas = ', '.join(numeros_string)
#e os ensine por pantalla en orde inversa separados por comas
print(numeros_separados_por_comas)
