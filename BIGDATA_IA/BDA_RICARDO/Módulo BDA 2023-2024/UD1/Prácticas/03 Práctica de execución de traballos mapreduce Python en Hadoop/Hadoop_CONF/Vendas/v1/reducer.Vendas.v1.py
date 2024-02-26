#!/usr/bin/python
import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    
    thisKey, thisSale = data_mapped
    
    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if oldKey and oldKey != thisKey:
        print(oldKey + "\t" + str(salesTotal))
        oldKey = thisKey
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

# Escribe o ultimo par, unha vez rematado o bucle
if oldKey is not None:
    print(oldKey + "\t" + str(salesTotal))
