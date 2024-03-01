#!/usr/bin/python3

import random


ROCK = 'piedra'
PAPER = 'papel'
SCISSORS = 'tijeras'


def evaluar_juego(accion_usuario, accion_computadora):
    if accion_usuario == accion_computadora:
        print(f"El usuario y la computadora seleccionaron {accion_usuario}. ¡Empate!")

    # El usuario eligió Piedra
    elif accion_usuario == ROCK:
        if accion_computadora == SCISSORS:
            print("La piedra aplasta las tijeras. ¡Ganaste!")
        else:
            print("El papel cubre la piedra. ¡Perdiste!")

    # El usuario eligió Papel
    elif accion_usuario == PAPER:
        if accion_computadora == ROCK:
            print("El papel cubre la piedra. ¡Ganaste!")
        else:
            print("Las tijeras cortan el papel. ¡Perdiste!")

    # El usuario eligió Tijeras
    elif accion_usuario == SCISSORS:
        if accion_computadora == ROCK:
            print("La piedra aplasta las tijeras. ¡Perdiste!")
        else:
            print("Las tijeras cortan el papel. ¡Ganaste!")


def main():
    acciones_juego = [ROCK, PAPER, SCISSORS]

    while True:
        accion_usuario = input("\nElige una opción: piedra, papel o tijeras: ")
        accion_computadora = random.choice(acciones_juego)

        print(f"\nSeleccionaste {accion_usuario}. La computadora seleccionó {accion_computadora}\n")
        evaluar_juego(accion_usuario, accion_computadora)


if __name__ == "__main__":
    main()
