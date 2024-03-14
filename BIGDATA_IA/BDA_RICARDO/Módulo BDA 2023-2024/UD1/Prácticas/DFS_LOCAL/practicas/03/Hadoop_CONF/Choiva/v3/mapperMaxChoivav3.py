#!/usr/bin/env python3

# -*- coding: iso-8859-15 -*-
'''
O formato de cada liña do ficheiro de entrada é:
"Código validación","Data","Código parámetro","Parámetro","Valor","Unidades"
Obxectivo: Obter, a partir do rexistro histórico, a cantidade de choiva diaria
para cada lectura e devolvelo precedido de só o número de ano
Para cada lectura obtemo-los pares <ano, choiva_recollida>
p.e.: 2023 4.2
'''
import sys
# Iterar sobre as liñas de entrada dende sys.stdin
for linha in sys.stdin:
# Eliminar espazos en branco ó principio e ó final da liña
linha = linha.strip()
# Descompo-la liña en campos separados por comas
codigo, instante_lectura, lixo1, lixo2, choiva, lixo3 = linha.split(",")
# Verificar se o string de código (eliminando as comiñas) está na lista ["1",
"5"]
if codigo.strip('"') in ["1", "5"]:
# Imprimi-lo ano e a cantidade de choiva
print(instante_lectura[1:5],choiva.strip('"'))
