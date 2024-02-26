#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import locale

locale.setlocale(locale.LC_ALL, '')

salesTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    
    thisKey, thisSale = data_mapped
    
    if oldKey and oldKey != thisKey:
        salesTotalFormatted = locale.currency(salesTotal, grouping=True)
        print("{}\t{}".format(oldKey, salesTotalFormatted))
        oldKey = thisKey
        salesTotal = 0
    
    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey is not None:
    salesTotalFormatted = locale.currency(salesTotal, grouping=True)
    print("{}\t{}".format(oldKey, salesTotalFormatted))