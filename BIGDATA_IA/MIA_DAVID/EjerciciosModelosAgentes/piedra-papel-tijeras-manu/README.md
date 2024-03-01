## O problema

El problema que abordamos es el juego clásico de "piedra, papel, tijeras" (RPS). En este juego, dos jugadores eligen entre tres opciones: piedra, papel o tijeras. Las reglas son simples: la piedra vence a las tijeras, las tijeras vencen al papel y el papel vence a la piedra. Si ambos jugadores eligen la misma opción, el juego es un empate.

### Implementación básica del juego RPS

Para abordar este problema, hemos implementado una solución básica en Python que permite a un agente jugar contra un oponente humano o contra un oponente que elige sus acciones al azar.

[Código básico del juego RPS](https://github.com/mpadinrepo/BIGDATA_IA/tree/main/BIGDATA_IA/MIA_DAVID/EjerciciosModelosAgentes/piedra-papel-tijeras-manu/01_RPS_Basico.py)


### Características del problema RPS

Para entender mejor el problema, debemos considerar sus características según el epígrafe "2.3.2 Properties of task environments" del libro IA: A modern approach:

| Contorno de tareas | Observable | Axentes | Determinista | Episódico | Estático | Discreto | Conocido |
|---------------------|------------|---------|--------------|-----------|----------|----------|----------|
| RPS                 | Sí         | 2       | Sí           | Sí        | Sí       | Sí       | Sí       |

**Justificación:**

- **Observable:** El estado del juego es completamente observable por ambos jugadores en todo momento. Cada jugador conoce las acciones elegidas por su oponente y el estado actual del juego.
- **Axentes:** En el juego RPS, hay dos agentes involucrados: un agente humano y un agente computacional. Ambos participantes toman decisiones durante el juego.
- **Determinista:** Dado un estado del juego y las acciones elegidas por ambos jugadores, el resultado del juego siempre es determinado. No hay elementos de azar en las reglas del juego RPS.
- **Episódico:** Cada juego de RPS es un episodio independiente. No hay dependencia entre juegos anteriores y juegos futuros. Cada juego se completa en un conjunto finito de pasos y tiene un resultado final.
- **Estático:** El entorno del juego no cambia durante la ejecución de un juego particular. Las reglas del juego RPS permanecen constantes y no se modifican durante el juego.
- **Discreto:** Las acciones disponibles para cada jugador (piedra, papel, tijeras) son opciones discretas y finitas. No hay acciones continuas ni infinitas disponibles en el juego.
- **Conocido:** Los jugadores conocen las reglas del juego y las posibles acciones disponibles en todo momento. No hay información oculta o desconocida para los jugadores durante el juego.

Estas características hacen que el juego "piedra, papel, tijeras" sea un entorno de tarea bien definido y adecuado para la implementación de un agente inteligente.

### Estrutura do axente

Para el desarrollo de la Estrutura do axente, podemos seguir el modelo general de un agente inteligente propuesto en el libro "IA: A Modern Approach" de Russell & Norvig. Este modelo incluye varios componentes que son comunes en la mayoría de los sistemas de agentes inteligentes.

#### Estrutura do axente para el juego de "piedra, papel, tijeras":

- **Percepción:** El agente recibe una percepción del entorno, que en este caso sería la acción del oponente en el turno anterior.
- **Memoria:** El agente puede mantener un registro de las acciones pasadas del oponente y sus propias acciones.
- **Selección de acción:** Basándose en la percepción y la memoria, el agente decide qué acción tomar en el siguiente turno.
- **Actuación:** El agente realiza la acción seleccionada, que en este caso sería elegir entre piedra, papel o tijeras.

#### Componentes del agente:

- **Percepción:** El agente necesita ser capaz de observar la acción del oponente en el turno anterior para poder tomar decisiones informadas.
- **Memoria:** El agente debe mantener un registro de las acciones pasadas del oponente y sus propias acciones para poder detectar patrones en el comportamiento del oponente.
- **Algoritmo de selección de acción:** Este algoritmo determina cómo el agente elige su próxima acción. Puede ser reactivo, basado en modelos, basado en objetivos o basado en utilidad, dependiendo de la estrategia del agente.
- **Actuación:** El agente realiza la acción seleccionada en el juego, que en este caso sería elegir entre piedra, papel o tijeras.

#### Modelo general de agente inteligente:

![Modelo general axente intelixente](enlace-a-imagen-modelo-axente-intelixente)

En este modelo, la percepción y la memoria se utilizan para recopilar información sobre el entorno y el historial de acciones. La selección de acción utiliza esta información para determinar la próxima acción del agente, que se lleva a cabo mediante la actuación.

Este enfoque permite que el agente tome decisiones informadas basadas en su comprensión del entorno y su experiencia pasada. La implementación de cada componente puede variar según la estrategia específica del agente y los detalles del entorno del juego.

Es importante señalar que, para el juego de "piedra, papel, tijeras", el agente puede utilizar diferentes estrategias de selección de acción, como elegir aleatoriamente, seguir una estrategia fija o adaptarse según el comportamiento del oponente. La elección de la estrategia depende de los objetivos y la complejidad del juego.

### Implementación en Python

A continuación, proporcionaremos un esquema básico de cómo podríamos implementar estos componentes en Python:

```python
class AgenteJugador:
    def __init__(self):
        self.ultima_accion_oponente = None

    def percibir_entorno(self, accion_oponente):
        self.ultima_accion_oponente = accion_oponente

    def seleccionar_accion(self):
        if self.ultima_accion_oponente is None:
            # En la primera jugada, elegir aleatoriamente
            return random.choice(['piedra', 'papel', 'tijeras'])
        else:
            # Implementar la estrategia del agente
            return self.manejar_accion_oponente(self.ultima_accion_oponente)

    def manejar_accion_oponente(self, accion_oponente):
        # Lógica para seleccionar la acción del agente
        # Puede ser una estrategia fija o adaptativa
        # Aquí se puede implementar la tabla de decisión del agente
        # basada en la acción del oponente y la historia del juego
        pass
Principios SOLID
Para garantizar que nuestro código sea mantenible y escalable, es importante aplicar los principios SOLID. Especialmente, nos centraremos en el Principio de Responsabilidad Única (SRP) y el Principio de Abierto/Cerrado (OCP). Esto implica diseñar nuestras clases de manera que tengan una única responsabilidad y que estén abiertas a la extensión pero cerradas a la modificación.

En la implementación de nuestro agente, esto se traduce en separar claramente las responsabilidades de percepción del entorno, selección de acción y manejo de la acción del oponente en métodos distintos. Además, podemos diseñar la clase de manera que sea fácil de extender para incluir nuevas estrategias de selección de acción en el futuro.

Con estos principios en mente, podemos escribir un código limpio, modular y fácil de mantener para nuestro agente inteligente.