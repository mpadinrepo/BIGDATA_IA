#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function  # Para compatibilidad de Python 2 y 3
import sys
import locale

locale.setlocale(locale.LC_ALL, '')

salesTotal = 0
salesMax = 0
oldKey = None
category_total = {}
payment_max = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        
        if item in category_total:
            category_total[item] += float(cost)
        else:
            category_total[item] = float(cost)
        
        if float(cost) > payment_max:
            payment_max = float(cost)
        
        if float(cost) > salesMax:
            salesMax = float(cost)
        
        salesTotal += float(cost)

for category, total in category_total.items():
    total_formatted = locale.currency(total, grouping=True)
    print('Categoría: {}\tTotal de ventas: {}'.format(category, total_formatted))

print('Máximo absoluto de todas las ventas: {}'.format(locale.currency(salesMax, grouping=True)))
print('Total de ventas: {}'.format(locale.currency(salesTotal, grouping=True)))
print('Venta más alta por tipo de pago: {}'.format(locale.currency(payment_max, grouping=True)))
