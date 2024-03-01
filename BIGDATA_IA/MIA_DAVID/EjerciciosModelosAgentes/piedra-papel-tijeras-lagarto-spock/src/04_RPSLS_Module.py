#!/usr/bin/python3

import random


class AccionJuego:

    acciones_rps = {
        'piedra': {'gana_a': 'tijeras', 'perdida_por': 'papel'},
        'papel': {'gana_a': 'piedra', 'perdida_por': 'tijeras'},
        'tijeras': {'gana_a': 'papel', 'perdida_por': 'piedra'}
    }

    acciones_rpsls = {
        'piedra': {'gana_a': ['tijeras', 'lagarto'], 'perdida_por': ['papel', 'spock']},
        'papel': {'gana_a': ['piedra', 'spock'], 'perdida_por': ['tijeras', 'lagarto']},
        'tijeras': {'gana_a': ['papel', 'lagarto'], 'perdida_por': ['piedra', 'spock']},
        'lagarto': {'gana_a': ['papel', 'spock'], 'perdida_por': ['piedra', 'tijeras']},
        'spock': {'gana_a': ['piedra', 'tijeras'], 'perdida_por': ['papel', 'lagarto']}
    }


def evaluar_juego(accion_usuario, accion_computadora, tipo_juego='rps'):
    if accion_usuario == accion_computadora:
        print(f"Tanto el usuario como la computadora eligieron {accion_usuario}. ¡Empate!")
    elif accion_usuario in getattr(AccionJuego, f'acciones_{tipo_juego}'):
        if accion_computadora in getattr(AccionJuego, f'acciones_{tipo_juego}')[accion_usuario]['gana_a']:
            print(f"{accion_usuario.capitalize()} vence a {accion_computadora}. ¡Ganaste!")
        else:
            print(f"{accion_computadora.capitalize()} vence a {accion_usuario}. ¡Perdiste!")
    else:
        print("¡Opción inválida!")


def obtener_accion_computadora():
    acciones = list(getattr(AccionJuego, f'acciones_rps'))
    accion_computadora = random.choice(acciones)
    print(f"La computadora eligió {accion_computadora}.")
    return accion_computadora


def obtener_accion_usuario():
    accion_usuario = input("\nElige una opción: piedra, papel, tijeras, lagarto o spock: ").lower()
    return accion_usuario


def jugar_otra_ronda():
    otra_ronda = input("\n¿Otra ronda? (s/n): ")
    return otra_ronda.lower() == 's'


def main():
    tipo_juego = input("Elige el tipo de juego: rps (Piedra, Papel, Tijeras) o rpsls (Piedra, Papel, Tijeras, Lagarto, Spock): ").lower()
    while tipo_juego not in ['rps', 'rpsls']:
        print("Tipo de juego inválido. Elige entre rps y rpsls.")
        tipo_juego = input("Elige el tipo de juego: rps o rpsls: ").lower()

    while True:
        accion_usuario = obtener_accion_usuario()
        accion_computadora = obtener_accion_computadora()
        evaluar_juego(accion_usuario, accion_computadora, tipo_juego)
        if not jugar_otra_ronda():
            break


if __name__ == "__main__":
    main()
