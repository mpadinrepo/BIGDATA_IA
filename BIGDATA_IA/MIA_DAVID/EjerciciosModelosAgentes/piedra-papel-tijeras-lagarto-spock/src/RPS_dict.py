#!/usr/bin/python3

import random


class AccionJuego:

    acciones = {
        'piedra': {'vence': 'tijeras', 'vencida_por': 'papel'},
        'papel': {'vence': 'piedra', 'vencida_por': 'tijeras'},
        'tijeras': {'vence': 'papel', 'vencida_por': 'piedra'}
    }


def evaluar_juego(accion_usuario, accion_computadora):
    if accion_usuario == accion_computadora:
        print(f"El usuario y la computadora eligieron {accion_usuario}. ¡Empate!")
    elif accion_usuario in AccionJuego.acciones:
        if accion_computadora == AccionJuego.acciones[accion_usuario]['vence']:
            print(f"{accion_usuario.capitalize()} vence a {accion_computadora}. ¡Ganaste!")
        else:
            print(f"{accion_computadora.capitalize()} vence a {accion_usuario}. ¡Perdiste!")
    else:
        print("¡Opción inválida!")


def obtener_accion_computadora():
    accion_computadora = random.choice(list(AccionJuego.acciones.keys()))
    print(f"La computadora eligió {accion_computadora}.")
    return accion_computadora


def obtener_accion_usuario():
    accion_usuario = input("\nElige una opción: piedra, papel o tijeras: ").lower()
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
