#!/usr/bin/python3

import random

ROCK = 'piedra'
PAPEL = 'papel'
TIJERAS = 'tijeras'
LAGARTO = 'lagarto'
SPOCK = 'Spock'

def evaluar_juego(accion_usuario, accion_computadora):
    if accion_usuario == accion_computadora:
        print(f"Tanto el usuario como la computadora eligieron {accion_usuario}. ¡Empate!")
    elif (accion_usuario, accion_computadora) in [(ROCK, TIJERAS), (ROCK, LAGARTO), 
                                                   (PAPEL, ROCK), (PAPEL, SPOCK), 
                                                   (TIJERAS, PAPEL), (TIJERAS, LAGARTO), 
                                                   (LAGARTO, PAPEL), (LAGARTO, SPOCK), 
                                                   (SPOCK, ROCK), (SPOCK, TIJERAS)]:
        print(f"¡{accion_usuario} vence a {accion_computadora}! ¡Ganaste!")
    else:
        print(f"¡{accion_computadora} vence a {accion_usuario}! ¡Perdiste!")

def main():
    acciones = [ROCK, PAPEL, TIJERAS, LAGARTO, SPOCK]
    while True:
        accion_usuario = input("\nElige una opción: piedra, papel, tijeras, lagarto o Spock: ")
        if accion_usuario.lower() in [ROCK.lower(), PAPEL.lower(), TIJERAS.lower(), 
                                      LAGARTO.lower(), SPOCK.lower()]:
            accion_computadora = random.choice(acciones)
            print(f"\nElegiste {accion_usuario}. La computadora eligió {accion_computadora}\n")
            evaluar_juego(accion_usuario.lower(), accion_computadora.lower())
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
