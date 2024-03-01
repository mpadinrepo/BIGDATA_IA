#!/usr/bin/python3

import random
from enum import Enum


class Accion(Enum):

    Piedra = 'piedra'
    Papel = 'papel'
    Tijeras = 'tijeras'


def evaluar_juego(accion_usuario, accion_computadora):
    if accion_usuario == accion_computadora:
        print(f"El usuario y la computadora seleccionaron {accion_usuario}. ¡Empate!")

    # El usuario eligió Piedra
    elif accion_usuario == Accion.Piedra:
        if accion_computadora == Accion.Tijeras:
            print("La piedra aplasta las tijeras. ¡Ganaste!")
        else:
            print("El papel cubre la piedra. ¡Perdiste!")

    # El usuario eligió Papel
    elif accion_usuario == Accion.Papel:
        if accion_computadora == Accion.Piedra:
            print("El papel cubre la piedra. ¡Ganaste!")
        else:
            print("Las tijeras cortan el papel. ¡Perdiste!")

    # El usuario eligió Tijeras
    elif accion_usuario == Accion.Tijeras:
        if accion_computadora == Accion.Piedra:
            print("La piedra aplasta las tijeras. ¡Perdiste!")
        else:
            print("Las tijeras cortan el papel. ¡Ganaste!")


def obtener_accion_computadora():
    accion_computadora = random.choice(list(Accion))
    print(f"La computadora seleccionó {accion_computadora.value}.")

    return accion_computadora


def obtener_accion_usuario():
    accion_usuario = input("\nElige una opción: piedra, papel o tijeras: ").lower()
    accion_usuario = Accion(accion_usuario)

    return accion_usuario


def jugar_otra_ronda():
    otra_ronda = input("\n¿Otra ronda? (s/n): ")
    return otra_ronda.lower() == 's'


def main():

    while True:
        accion_usuario = obtener_accion_usuario()
        accion_computadora = obtener_accion_computadora()
        evaluar_juego(accion_usuario, accion_computadora)

        if not jugar_otra_ronda():
            break


if __name__ == "__main__":
    main()
