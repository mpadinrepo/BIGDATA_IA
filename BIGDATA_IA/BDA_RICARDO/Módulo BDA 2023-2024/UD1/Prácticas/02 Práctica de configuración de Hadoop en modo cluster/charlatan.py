#!/usr/bin/env python3

# charlatan.py
# charlatan crea un ficheiro de texto con palabras pseudoaleatorias que se toman 
# dunha lista que pode definir o/a programador/a
#
# Pode definirse o número de palabras para crear un ficheiro máis grande

import random

ficheiro = open("charla.txt","a") 
pseudoPalabrasAleatorias = ["Saraiba ", "Pachuzo ", "Chorima ", "Moraima ", "Luscofusco ", "Licorka ", "Fume "]
cantidadePalabrasAleatorias = len(pseudoPalabrasAleatorias) - 1

#Aumenta NUMERO_PALABRAS_RESULTANTES para crear un ficheiro maior
#15000000 -> 112MB
#30000000 -> 231MB
NUMERO_PALABRAS_RESULTANTES = 30000000

indice = 0
for x in range(NUMERO_PALABRAS_RESULTANTES):
   indice = random.randint(0,cantidadePalabrasAleatorias)
   ficheiro.write(pseudoPalabrasAleatorias[indice])
   if x % 20 == 0:
      ficheiro.write('\n')
