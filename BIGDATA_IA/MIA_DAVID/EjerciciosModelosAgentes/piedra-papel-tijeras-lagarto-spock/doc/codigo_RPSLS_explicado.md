Código RPSLS: Piedra, Papel, Tijeras, Lagarto, Spock


# RPSLS: Piedra, Papel, Tijeras, Lagarto, Spock

## Descripción
Este proyecto implementa el juego "Piedra, Papel, Tijeras, Lagarto, Spock" (RPSLS) en Python. El juego es una extensión del clásico juego "Piedra, Papel, Tijeras" (RPS), e incluye dos diccionarios para definir las reglas del juego: `acciones_rps` para RPS y `acciones_rpsls` para RPSLS.

## Funciones

1. **Definición de la clase AccionJuego**: La clase `AccionJuego` define dos diccionarios que especifican las acciones que vencen o son vencidas por otras en los juegos RPS y RPSLS.
    ```python
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
    ```

2. **Función evaluar_juego**: Toma las acciones del usuario y la computadora, así como el tipo de juego (RPS o RPSLS), y determina el resultado del juego según las reglas definidas.
    ```python
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
    ```

3. **Función obtener_accion_computadora**: Elige aleatoriamente una acción para la computadora a partir de las opciones disponibles en el juego.
    ```python
    def obtener_accion_computadora():
        acciones = list(getattr(AccionJuego, f'acciones_rps'))
        accion_computadora = random.choice(acciones)
        print(f"La computadora eligió {accion_computadora}.")
        return accion_computadora
    ```

4. **Función obtener_accion_usuario**: Solicita al usuario que elija una acción entre las opciones disponibles.
    ```python
    def obtener_accion_usuario():
        accion_usuario = input("\nElige una opción: piedra, papel, tijeras, lagarto o spock: ").lower()
        return accion_usuario
    ```

5. **Función jugar_otra_ronda**: Pregunta al usuario si desea jugar otra ronda y devuelve `True` si la respuesta es afirmativa.
    ```python
    def jugar_otra_ronda():
        otra_ronda = input("\n¿Otra ronda? (s/n): ")
        return otra_ronda.lower() == 's'
    ```

6. **Función main**: Controla el flujo principal del programa, permitiendo al usuario seleccionar el tipo de juego y jugar repetidamente hasta que decida salir.
    ```python
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
    ```

## Razonamiento y Consideraciones

- **Estructura de datos conveniente**: El uso de diccionarios para almacenar las reglas del juego facilita la consulta de qué acción vence a cuál, simplificando la lógica del programa y mejorando su mantenimiento.

- **Interacción con el usuario**: El programa interactúa amigablemente con el usuario, solicitando acciones y mostrando resultados de forma clara, lo que mejora la experiencia de juego.

- **Aleatoriedad en la elección de la computadora**: La elección aleatoria de las acciones de la computadora agrega un elemento de imprevisibilidad al juego, lo que lo hace más emocionante y desafiante para el usuario.

- **Manejo de entradas inválidas**: El programa maneja de manera efectiva las entradas inválidas del usuario, solicitando que vuelva a ingresar una opción válida hasta que lo haga correctamente. Esto mejora la robustez del programa y evita posibles errores.

## Uso

Para ejecutar el juego, simplemente ejecuta el script `04_RPSLS_Module.py` y sigue las instrucciones en pantalla para seleccionar el tipo de juego y jugar.

## Razonamiento y Consideraciones Adicionales

- **Estructura de datos flexible**: La implementación de las reglas del juego mediante diccionarios permite una fácil expansión del juego, facilitando la adición de nuevas acciones y reglas en el futuro.

- **Legibilidad del código**: El código está escrito de manera clara y legible, utilizando nombres descriptivos de variables y funciones, lo que facilita su comprensión y mantenimiento por parte de otros desarrolladores.

- **Modularidad**: El código está organizado en funciones independientes, cada una con una responsabilidad específica, lo que facilita su reutilización en otros proyectos o la realización de pruebas unitarias.

- **Documentación**: Se proporciona una descripción clara de cada función y su propósito, lo que ayuda a los desarrolladores a entender rápidamente cómo funciona el programa y cómo utilizarlo adecuadamente.
