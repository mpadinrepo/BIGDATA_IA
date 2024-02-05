""" 
Escribir un programa que pida  ao usuario ou  seu peso (en kg) e estatura (en centímetros),
calcule ou índice de masa corporal e  o almacene  nunha variable, e  mostre por pantalla a frase:
O  teu índice de masa corporal  é <imc>  onde <imc>  é o índice de masa corporal calculado redondeado con  dous  decimais. """

peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su altura en centímetros: "))
estatura_en_metros = estatura / 100
imc = peso / (estatura_en_metros ** 2)
imcredondeado = round(imc, 2)

print('Peso:', peso, 'kg')
print('Estatura:', estatura, 'cm')
print('El IMC según el peso y altura indicada es:', imcredondeado)