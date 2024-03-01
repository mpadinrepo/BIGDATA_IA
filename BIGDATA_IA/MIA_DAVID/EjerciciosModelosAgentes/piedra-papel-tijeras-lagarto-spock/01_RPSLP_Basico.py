#!/usr/bin/python3

import random

ROCK = 'piedra'
PAPEL = 'papel'
TIJERAS = 'tijeras'

def evaluar_juego(accion_usuario, accion_computadora):
    if accion_usuario == accion_computadora:
        print(f"Tanto el usuario como la computadora eligieron {accion_usuario}. ¡Empate!")
    elif accion_usuario == ROCK:
        if accion_computadora == TIJERAS:
            print("La piedra rompe las tijeras. ¡Ganaste!")
        else:
            print("El papel cubre la piedra. ¡Perdiste!")
    elif accion_usuario == PAPEL:
        if accion_computadora == ROCK:
            print("El papel cubre la piedra. ¡Ganaste!")
        else:
            print("Las tijeras cortan el papel. ¡Perdiste!")
    elif accion_usuario == TIJERAS:
        if accion_computadora == ROCK:
            print("La piedra rompe las tijeras. ¡Perdiste!")
        else:
            print("Las tijeras cortan el papel. ¡Ganaste!")

def main():
    acciones = [ROCK, PAPEL, TIJERAS]
    while True:
        accion_usuario = input("\nElige una opción: piedra, papel o tijeras: ")
        accion_computadora = random.choice(acciones)
        print(f"\nElegiste {accion_usuario}. La computadora eligió {accion_computadora}\n")
        evaluar_juego(accion_usuario, accion_computadora)

if __name__ == "__main__":
    main()
