# O problema

El problema que abordamos es el juego clásico de **"piedra, papel, tijeras"** (RPS) y su extensión **"piedra, papel, tijeras, lagarto, Spock"** (RPSLS). En estos juegos, dos jugadores eligen entre diferentes opciones y las reglas determinan cuál opción gana. En RPS, las opciones son piedra, papel y tijeras, mientras que en RPSLS se agregan lagarto y Spock. Las reglas son simples y predefinidas: 
- La piedra aplasta las tijeras
- Las tijeras cortan el papel
- El papel cubre la piedra
- La piedra aplasta al lagarto
- El lagarto envenena a Spock
- Spock rompe las tijeras
- Las tijeras decapitan al lagarto
- El lagarto come el papel
- El papel desaprueba a Spock
- Spock vaporiza la piedra

Si ambos jugadores eligen la misma opción, el juego es un empate.

### Implementación básica del juego RPS

Hemos implementado una solución básica en Python que permite a un agente jugar contra un oponente humano o contra un oponente que elige sus acciones al azar.

- [Código básico del juego RPS](BIGDATA_IA/BIGDATA_IA/MIA_DAVID/EjerciciosModelosAgentes/piedra-papel-tijeras-manu/01_RPS_Basico.py)
- [Código básico del juego RPSLS](BIGDATA_IA/BIGDATA_IA/MIA_DAVID/EjerciciosModelosAgentes/piedra-papel-tijeras-lagarto-spock/01_RPSLP_Basico.py)

### Características del problema RPS y RPSLS

Para entender mejor el problema, debemos considerar sus características según el epígrafe **"2.3.2 Properties of task environments"** del libro **IA: A modern approach**:

| Contorno de tareas | Observable | Axentes | Determinista | Episódico | Estático | Discreto | Conocido |
|---------------------|------------|---------|--------------|-----------|----------|----------|----------|
| RPS                 | Sí         | 2       | Sí           | Sí        | Sí       | Sí       | Sí       |
| RPSLS               | Sí         | 2       | Sí           | Sí        | Sí       | Sí       | Sí       |

**Justificación:**
- **Observable:** El estado del juego es completamente observable por ambos jugadores en todo momento. Cada jugador conoce las acciones elegidas por su oponente y el estado actual del juego.
- **Axentes:** En el juego RPS y RPSLS, hay dos agentes involucrados: un agente humano y un agente computacional. Ambos participantes toman decisiones durante el juego.
- **Determinista:** Dado un estado del juego y las acciones elegidas por ambos jugadores, el resultado del juego siempre es determinado. No hay elementos de azar en las reglas de los juegos RPS y RPSLS.
- **Episódico:** Cada juego de RPS y RPSLS es un episodio independiente. No hay dependencia entre juegos anteriores y juegos futuros. Cada juego se completa en un conjunto finito de pasos y tiene un resultado final.
- **Estático:** El entorno del juego no cambia durante la ejecución de un juego particular. Las reglas de los juegos RPS y RPSLS permanecen constantes y no se modifican durante el juego.
- **Discreto:** Las acciones disponibles para cada jugador en RPS y RPSLS son opciones discretas y finitas. No hay acciones continuas ni infinitas disponibles en los juegos.
- **Conocido:** Los jugadores conocen las reglas de los juegos y las posibles acciones disponibles en todo momento. No hay información oculta o desconocida para los jugadores durante los juegos.

Estas características hacen que los juegos **"piedra, papel, tijeras"** y **"piedra, papel, tijeras, lagarto, Spock"** sean entornos de tarea bien definidos y adecuados para la implementación de un agente inteligente.

### Estrutura do axente

Para el desarrollo de la Estrutura do axente, podemos seguir el modelo general de un agente inteligente propuesto en el libro **"IA: A Modern Approach"** de Russell & Norvig.

#### Estrutura do axente para el juego de "piedra, papel, tijeras" y "piedra, papel, tijeras, lagarto, Spock":

- **Percepción:** El agente recibe una percepción del entorno, que en este caso sería la acción del oponente en el turno anterior.
- **Memoria:** El agente puede mantener un registro de las acciones pasadas del oponente y sus propias acciones.
- **Selección de acción:** Basándose en la percepción y la memoria, el agente decide qué acción tomar en el siguiente turno.
- **Actuación:** El agente realiza la acción seleccionada, que en este caso sería elegir entre las opciones disponibles en los juegos.

#### Componentes del agente:

- **Percepción:** El agente necesita ser capaz de observar la acción del oponente en el turno anterior para poder tomar decisiones informadas.
- **Memoria:** El agente debe mantener un registro de las acciones pasadas del oponente y sus propias acciones para poder detectar patrones en el comportamiento del oponente.
- **Algoritmo de selección de acción:** Este algoritmo determina cómo el agente elige su próxima acción. Puede ser reactivo, basado en modelos, basado en objetivos o basado en utilidad, dependiendo de la estrategia del agente.
- **Actuación:** El agente realiza la acción seleccionada en el juego.

#### Modelo general de agente inteligente:

![Modelo general axente intelixente](enlace-a-imagen-modelo-axente-intelixente)

En este modelo, la percepción y la memoria se utilizan para recopilar información sobre el entorno y el historial de acciones. La selección de acción utiliza esta información para determinar la próxima acción del agente, que se lleva a cabo mediante la actuación.

Este enfoque permite que el agente tome decisiones informadas basadas en su comprensión del entorno y su experiencia pasada. La implementación de cada componente puede variar según la estrategia específica del agente y los detalles del entorno del juego.

Es importante señalar que, para los juegos de **"piedra, papel, tijeras"** y **"piedra, papel, tijeras, lagarto, Spock"**, el agente puede utilizar diferentes estrategias de selección de acción, como elegir aleatoriamente, seguir una estrategia fija o adaptarse según el comportamiento del oponente. La elección de la estrategia depende de los objetivos y la complejidad del juego.

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
            return random.choice(['piedra', 'papel', 'tijeras', 'lagarto', 'Spock'])
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
