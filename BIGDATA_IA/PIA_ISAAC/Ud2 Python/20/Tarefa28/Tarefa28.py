""" Tarefa 28
Escribir un programa que pida ao usuario dous números enteiros 
e mostre por pantalla a < n> entre < m> dá un  cociente < c> e un resto < r> onde < n> e < m> son os números introducidos polo usuario,
e < c> e < r> son o  cociente e o resto da división enteira respectivamente.

Neste exercicio se trata de prácticar o uso de tuplas. 
Na función que fagas para implementar a división terás como parámetros o dividende o mailo divisor,
e vas calcular o dividendo e máis o resto. Como só podes devolver no return un elemento terás que empaquetar a resposta nunha tupla.
No programa principal podes chamar a esa función, recoller o resultado e acceder á tupla devolta para facer a impresión en pantalla. """

recolectorN = int(input ('Introduce el dividendo :'))
recolectorM= int(input ('Introduce el divisor :'))
def division_con_resto(dividendo,divisor):
    cociente=dividendo//divisor
    resto =dividendo % divisor
    return cociente,resto
resultado = division_con_resto(recolectorN, recolectorM)

cociente, resto = resultado
print(f"{recolectorN} entre {recolectorM} da un cociente {cociente} e un resto {resto}.")