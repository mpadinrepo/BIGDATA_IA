#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-

'''
O formato de cada liña do ficheiro de entrada é:
- un número enteiro de 4 díxitos correspondente ó ano,
- un espazo en branco e
- un número real correspondente ás choivas en litros/metro cadrado
p.e: 2023 24.6
Obxectivo: calcula-la cantidade de choiva máxima diaria de cada ano a partir do
rexistro histórico
p.e.: 2018 39.0
'''

import sys

# Inicializar variables
ano_actual = None
choiva_maxima_actual = None

# Ler a primeira liña fóra do bucle para evitar comprobar sempre se é
# a primeira liña para cada novo rexistro lido
primeira_linha = sys.stdin.readline()

# Descompo-la primeira liña
ano_actual, choiva_maxima_actual = primeira_linha.strip().split(" ", 1)
choiva_maxima_actual = float(choiva_maxima_actual)

# Iterar sobre as demais liñas de entrada
for linha in sys.stdin:
    ano, choiva_str = linha.strip().split(" ", 1)
    # Converte-la cantidade de choiva a float
    choiva = float(choiva_str)
    
    # Se é o mesmo ano, comprobar se a cantidade de choiva é a máxima
    if ano_actual == ano:
        choiva_maxima_actual = max(choiva_maxima_actual, choiva)
    else:
        # Se cambia o ano, emitir resultado e actualizar variables
        print("%s\t%s" % (ano_actual, choiva_maxima_actual))
        ano_actual = ano
        choiva_maxima_actual = choiva

# Emiti-lo resultado do último ano
if ano_actual is not None:
    print("%s\t%s" % (ano_actual, choiva_maxima_actual))
