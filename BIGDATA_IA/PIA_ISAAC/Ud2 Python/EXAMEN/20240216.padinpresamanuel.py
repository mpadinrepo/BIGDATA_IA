""" Proba 1.
Exercicio 1 (2 puntos)

Para comprobar se está correcto hai que coller os 8 díxitos, interpretalos coma un número e calcular
o resto da división do número entre 23. 

O que nos vai dar coma resultado un número entre 0 e 22. A asociación de letras é como se presenta na seguinte
táboa.
RESTO 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
LETRA T R W A G M Y F P D X B N J Z S Q V H L C K E

Fai un programa que pida ao usuario 

un número de DNI coa letra e indique se é correcto ou non, 
para o que deberás calcular a letra que lle corresponde ao número e verificar que coincida coa letra proporcionada polo usuario.

• Deberás verificar qué o número está composto por 8 dixitos e unha letra,
puidendo está estar en maiusculas ou minúsculas. 

Se non fose correcto indicarías que o formato non é o apropiado e parararías o programa.
(0,5
puntos)

• Se o formato é correcto deberás comprobar se a letra coincide co esperado,
indicando finalmente cunha mensaxe se o número era correcto ou non. (1
punto)

• Deberás crear ao menos algúns test que chequee a función que crees. (0,5
puntos)

Algúns DNI con letra para que fagas probas: 65004204V, 30022846A
Nos ficheiros que acompañan a proba tes unha lista de tuplas, onde
o primeiro elemento e o resto, e o segundo e a letra maiúscula que
lle toca.
"""

dninumero = int(input("Ingrese numero de DNI: "))
# numcaracteres = len(dninumero)
# print (numcaracteres)
# suma = sum(dninumero)
# print (suma)



def validacionDNI(dninumero):
    # Eliminar espacios y verificar longitud
    dninumero = dninumero.replace(" ", "")
    if len(dninumero) <= 8:
        raise ValueError("Número de DNI no válido: Longitud inválida")
    else:
        if len(dninumero)>9:
            print ("Número de DNI no válido: Longitud inválida")
        else
    # Verificar caracteres válidos
    if not dninumero.isdigit():
        raise ValueError("Número de DNI no válido: Caracteres no válidos")
    # Sumar todos los dígitos
    suma_digitos = sum(dninumero)
    # Verificar si la suma es divisible por 23
    if suma_digitos % 23 != 0:
        raise ValueError("Número de DNI no válido: La suma no es divisible por 10")
    # El número es válido
    return True