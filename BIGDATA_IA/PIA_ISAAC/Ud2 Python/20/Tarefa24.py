n = int(input("Ingrese un número entero positivo: "))

def calcular_suma(n):
    resultado = n * (n + 1) // 2
    return resultado
if n <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    suma = calcular_suma(n)
    print(f"La suma de enteros desde 1 hasta {n} es: {suma}")
