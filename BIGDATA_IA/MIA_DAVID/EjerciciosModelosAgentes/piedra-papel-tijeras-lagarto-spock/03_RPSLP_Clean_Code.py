#!/usr/bin/python3

import random
from enum import Enum

class Accion(Enum):
    PIEDRA = 'piedra'
    PAPEL = 'papel'
    TIJERAS = 'tijeras'

def evaluar_juego(accion_usuario, accion_computadora):
    global partidas_jugadas, partidas_ganadas, partidas_perdidas

    partidas_jugadas += 1

    if accion_usuario == accion_computadora:
        print(f"Tanto el usuario como la computadora eligieron {accion_usuario.name}. ¡Empate!")
    elif accion_usuario == Accion.PIEDRA:
        if accion_computadora == Accion.TIJERAS:
            print("La piedra rompe las tijeras. ¡Ganaste!")
            partidas_ganadas += 1
        else:
            print("El papel cubre la piedra. ¡Perdiste!")
            partidas_perdidas += 1
    elif accion_usuario == Accion.PAPEL:
        if accion_computadora == Accion.PIEDRA:
            print("El papel cubre la piedra. ¡Ganaste!")
            partidas_ganadas += 1
        else:
            print("Las tijeras cortan el papel. ¡Perdiste!")
            partidas_perdidas += 1
    elif accion_usuario == Accion.TIJERAS:
        if accion_computadora == Accion.PIEDRA:
            print("La piedra rompe las tijeras. ¡Perdiste!")
            partidas_perdidas += 1
        else:
            print("Las tijeras cortan el papel. ¡Ganaste!")
            partidas_ganadas += 1

def obtener_accion_computadora():
    return random.choice(list(Accion))

def obtener_accion_usuario():
    accion = input(f"\nElige una opción: {', '.join([accion.value for accion in Accion])}: ").lower()
    return Accion(accion)

def seguir_jugando():
    return input("\n¿Otra ronda? (s/n): ").lower() == 's'

def main():
    global partidas_jugadas, partidas_ganadas, partidas_perdidas

    partidas_jugadas = 0
    partidas_ganadas = 0
    partidas_perdidas = 0

    while True:
        try:
            accion_usuario = obtener_accion_usuario()
        except ValueError:
            print(f"Selección inválida. Elige una opción de: {[accion.value for accion in Accion]}!")
            continue
        accion_computadora = obtener_accion_computadora()
        evaluar_juego(accion_usuario, accion_computadora)
        print(f"\nPartidas jugadas: {partidas_jugadas}, Partidas ganadas: {partidas_ganadas}, Partidas perdidas: {partidas_perdidas}")
        if not seguir_jugando():
            break

if __name__ == "__main__":
    main()
