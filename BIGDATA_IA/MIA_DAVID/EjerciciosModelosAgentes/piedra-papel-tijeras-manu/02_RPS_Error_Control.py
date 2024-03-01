#!/usr/bin/python3

import random

ROCK = 'piedra'
PAPEL = 'papel'
TIJERAS = 'tijeras'

class OpcionIncorrectaException(Exception):
    pass

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
        try:
            accion_usuario = input("\nElige una opción: piedra, papel o tijeras: ").lower()
            if accion_usuario not in acciones:
                raise OpcionIncorrectaException
            accion_computadora = random.choice(acciones)
            print(f"\nElegiste {accion_usuario}. La computadora eligió {accion_computadora}\n")
            evaluar_juego(accion_usuario, accion_computadora)
        except OpcionIncorrectaException:
            print("\nSolo puedes elegir piedra, papel o tijeras!")

if __name__ == "__main__":
    main()
