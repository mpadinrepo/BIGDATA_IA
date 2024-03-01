Problema: Juego de Piedra, Papel, Tijeras (RPS)
El juego clásico de "piedra, papel, tijeras" (RPS) es un juego simple en el que dos jugadores eligen entre tres opciones: piedra, papel o tijeras. Las reglas son claras: la piedra vence a las tijeras, las tijeras vencen al papel y el papel vence a la piedra. Si ambos jugadores eligen la misma opción, el juego termina en empate.

Implementación Básica del Juego RPS
Para abordar este problema, hemos implementado una solución básica en Python que permite que un agente juegue contra un oponente humano o contra un oponente que elige sus acciones al azar.

Código básico del juego RPS
Características del Problema RPS
Según el epígrafe "2.3.2 Properties of task environments" del libro IA: A Modern Approach, podemos identificar las siguientes características del entorno del juego RPS:

Característica	Descripción
Observable	Sí. El estado del juego es completamente observable por ambos jugadores en todo momento.
Agentes	2. Hay dos agentes involucrados: un agente humano y un agente computacional.
Determinista	Sí. Dado un estado del juego y las acciones elegidas por ambos jugadores, el resultado del juego es determinado.
Episódico	Sí. Cada juego de RPS es un episodio independiente.
Estático	Sí. El entorno del juego no cambia durante la ejecución de un juego particular.
Discreto	Sí. Las acciones disponibles para cada jugador (piedra, papel, tijeras) son opciones discretas y finitas.
Conocido	Sí. Los jugadores conocen las reglas del juego y las posibles acciones disponibles en todo momento.
Contorno de Tareas RPS
El juego de RPS presenta un entorno observable, determinista, episódico, estático, discreto y conocido. Estas características hacen que sea un problema adecuado para la implementación de un agente inteligente.

Estrutura do Axente para RPS
La estructura del agente inteligente para el juego de RPS puede seguir el modelo general propuesto en IA: A Modern Approach:

Percepción: El agente recibe la acción del oponente en el turno anterior como percepción del entorno.
Memoria: El agente puede mantener un registro de las acciones pasadas del oponente y sus propias acciones.
Selección de Acción: Basándose en la percepción y la memoria, el agente decide qué acción tomar en el siguiente turno.
Actuación: El agente realiza la acción seleccionada (piedra, papel o tijeras) en el juego.
Implementación del Agente en Python
python
Copy code
class AgenteJugador:
    def __init__(self):
        self.ultima_accion_oponente = None

    def percibir_entorno(self, accion_oponente):
        self.ultima_accion_oponente = accion_oponente

    def seleccionar_accion(self):
        if self.ultima_accion_oponente is None:
            return random.choice(['piedra', 'papel', 'tijeras'])
        else:
            return self.manejar_accion_oponente(self.ultima_accion_oponente)

    def manejar_accion_oponente(self, accion_oponente):
        # Lógica para seleccionar la acción del agente
        pass
Esta es una implementación básica del agente. La función manejar_accion_oponente debe ser completada con la estrategia específica del agente.

Principios SOLID
Es importante aplicar los principios SOLID para garantizar que el código sea mantenible y escalable. Especialmente, nos centraremos en el Principio de Responsabilidad Única (SRP) y el Principio de Abierto/Cerrado (OCP), separando las responsabilidades y permitiendo la extensión del código.