#!/usr/bin/python3

import random


PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERAS = 'tijeras'


def evaluar_juego(accion_usuario, accion_computadora):
    if accion_usuario == accion_computadora:
        print(f"El usuario y la computadora seleccionaron {accion_usuario}. ¡Empate!")

    # El usuario eligió Piedra
    elif accion_usuario == PIEDRA:
        if accion_computadora == TIJERAS:
            print("La piedra aplasta las tijeras. ¡Ganaste!")
        else:
            print("El papel cubre la piedra. ¡Perdiste!")

    # El usuario eligió Papel
    elif accion_usuario == PAPEL:
        if accion_computadora == PIEDRA:
            print("El papel cubre la piedra. ¡Ganaste!")
        else:
            print("Las tijeras cortan el papel. ¡Perdiste!")

    # El usuario eligió Tijeras
    elif accion_usuario == TIJERAS:
        if accion_computadora == PIEDRA:
            print("La piedra aplasta las tijeras. ¡Perdiste!")
        else:
            print("Las tijeras cortan el papel. ¡Ganaste!")


def main():
    acciones_juego = [PIEDRA, PAPEL, TIJERAS]

    while True:
        accion_usuario = input("\nElige una opción: piedra, papel o tijeras: ")
        accion_computadora = random.choice(acciones_juego)

        print(f"\nSeleccionaste {accion_usuario}. La computadora seleccionó {accion_computadora}\n")
        evaluar_juego(accion_usuario, accion_computadora)


if __name__ == "__main__":
    main()
