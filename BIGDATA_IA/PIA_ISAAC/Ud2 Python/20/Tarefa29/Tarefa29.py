# Tarefa 29

# Unha xoguetería ten moito éxito en dous dos seus produtos: pallasos e bonecas.  V
# Adoita facer venda por correo e a empresa de loxística cóbralles por peso de cada
# paquete así que deben calcular o peso dos pallasos e bonecas que sairán en cada
# paquete a demanda. Cada pallaso pesa 112  g e cada boneca 75  g. 
# Escribir un programa que lea o número de pallasos e bonecas vendidos
# no último pedido e calcule o peso total en Kg do paquete que será enviado.


payasos = int(input('Ingrese el numero de Payasos del pedido: '))
munhecas = int(input('Ingrese el numero de Munhecas del pedido: '))

pesomunhecas = 75
pesopayasoskg= payasos * 112
pesopayasoskg = pesopayasoskg / 1000
pesomunhecaskg = munhecas * pesomunhecas / 1000
pesototalopedido=pesopayasoskg+pesomunhecaskg

print('Peso total de payasos en kg:', pesopayasoskg)
print('Peso total de munhecas en kg:', pesomunhecaskg)
print('Peso total de payasos y munhecas en kg es :', pesototalopedido ,'kg')