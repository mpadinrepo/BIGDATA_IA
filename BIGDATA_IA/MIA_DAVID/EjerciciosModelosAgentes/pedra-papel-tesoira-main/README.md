Práctica Axentes Intelixentes
=============================

   * [O problema](#o-problema)
   * [Contorno de tarefas](#tcontorno-de-tarefas)
   * [Estrutura do axente](#estrutura-do-axente)
   * [Implementación](#implementación)
   * [Extensión](#extensión)
   * [Entrega](#entrega)
   * [Bibliografía](#bibliografía)

Proponse programar un axente intelixente solución ao entorno de tarefas do xogo pedra, papel, tesoiras, seguindo as directrices de modelado propostas no capítulo 2 _Intelligent Agents_ do libro _IA: A modern approach, Russell & Norvig_.

Para iso é necesario:

1. Especificar as características do contorno de tarefas.
2. Identificar o tipo de axente para determinar a estrutura do axente.
3. Implementar en Python os compoñentes da estrutura do axente para construir a función axente ou función mapa.


## El problema:

El problema que abordamos es el juego clásico de "piedra, papel, tijeras" (RPS). En este juego, dos jugadores eligen entre tres opciones: piedra, papel o tijeras. Las reglas son simples: la piedra vence a las tijeras, las tijeras vencen al papel y el papel vence a la piedra. Si ambos jugadores eligen la misma opción, el juego es un empate.

Implementación básica del juego RPS
Para abordar este problema, hemos implementado una solución básica en Python que permite a un agente jugar contra un oponente humano o contra un oponente que elige sus acciones al azar.

El código básico del juego RPS se encuentra en el siguiente enlace: solución básica.

Características del problema RPS
Para entender mejor el problema, debemos considerar sus características según el epígrafe "2.3.2 Properties of task environments" del libro IA: A modern approach:

Observable: El estado del juego (las acciones elegidas por cada jugador) es completamente observable por ambos jugadores en todo momento.
Axentes: En el juego RPS, hay dos agentes: el agente humano y el agente computacional.
Determinista: Dado un estado del juego y las acciones elegidas por ambos jugadores, el resultado del juego siempre es determinado. No hay elementos de azar en las reglas del juego.
Episódico: Cada juego de RPS es un episodio independiente. No hay dependencia entre juegos anteriores y juegos futuros.
Estático: El entorno del juego (las reglas del juego) no cambia durante la ejecución de un juego particular.
Discreto: Las acciones disponibles para cada jugador (piedra, papel, tijeras) son opciones discretas y finitas.
Conocido: Los jugadores conocen las reglas del juego y las posibles acciones disponibles en todo momento.
En resumen, el juego RPS presenta un entorno observable, determinista, episódico, estático, discreto y conocido. Esto lo convierte en un problema adecuado para la implementación de un agente inteligente.

Continuaremos con la identificación del tipo de agente para determinar la estructura del agente en el siguiente apartado.

## Contorno de tarefas

En este apartado, especificamos las características del contorno de tareas del juego "piedra, papel, tijeras" (RPS) y justificamos nuestra respuesta de acuerdo con las pautas proporcionadas en el epígrafe "2.3.2 Properties of task environments" del libro IA: A modern approach.

Características del contorno de tareas del RPS

| Contorno de tareas | Observable | Axentes | Determinista | Episódico | Estático | Discreto | Conocido |
|---------------------|------------|---------|--------------|-----------|----------|----------|----------|
| RPS                 | Sí         | 2       | Sí           | Sí        | Sí       | Sí       | Sí       |


Justificación

Observable: El estado del juego es completamente observable por ambos jugadores en todo momento. Cada jugador conoce las acciones elegidas por su oponente y el estado actual del juego.

Axentes: En el juego RPS, hay dos agentes involucrados: un agente humano y un agente computacional. Ambos participantes toman decisiones durante el juego.

Determinista: Dado un estado del juego y las acciones elegidas por ambos jugadores, el resultado del juego siempre es determinado. No hay elementos de azar en las reglas del juego RPS.

Episódico: Cada juego de RPS es un episodio independiente. No hay dependencia entre juegos anteriores y juegos futuros. Cada juego se completa en un conjunto finito de pasos y tiene un resultado final.

Estático: El entorno del juego no cambia durante la ejecución de un juego particular. Las reglas del juego RPS permanecen constantes y no se modifican durante el juego.

Discreto: Las acciones disponibles para cada jugador (piedra, papel, tijeras) son opciones discretas y finitas. No hay acciones continuas ni infinitas disponibles en el juego.

Conocido: Los jugadores conocen las reglas del juego y las posibles acciones disponibles en todo momento. No hay información oculta o desconocida para los jugadores durante el juego.

Estas características hacen que el juego "piedra, papel, tijeras" sea un entorno de tarea bien definido y adecuado para la implementación de un agente inteligente. 

#### La observabilidad, determinismo y discreción del entorno facilitan la toma de decisiones por parte del agente.

## Estrutura do axente

Para el desarrollo de la Estrutura do axente, podemos seguir el modelo general de un agente inteligente propuesto en el libro "IA: A Modern Approach" de Russell & Norvig. Este modelo incluye varios componentes que son comunes en la mayoría de los sistemas de agentes inteligentes. Aquí se explica cómo podríamos adaptar este modelo al contexto del juego de "piedra, papel, tijeras":

Estrutura do axente para el juego de "piedra, papel, tijeras":

El agente inteligente para el juego de "piedra, papel, tijeras" podría seguir una estructura similar a la siguiente:

Percepción: El agente recibe una percepción del entorno, que en este caso sería la acción del oponente en el turno anterior.

Memoria: El agente puede mantener un registro de las acciones pasadas del oponente y sus propias acciones.

Selección de acción: Basándose en la percepción y la memoria, el agente decide qué acción tomar en el siguiente turno.

Actuación: El agente realiza la acción seleccionada, que en este caso sería elegir entre piedra, papel o tijeras.

Componentes del agente:

Percepción: El agente necesita ser capaz de observar la acción del oponente en el turno anterior para poder tomar decisiones informadas.

Memoria: El agente debe mantener un registro de las acciones pasadas del oponente y sus propias acciones para poder detectar patrones en el comportamiento del oponente.

Algoritmo de selección de acción: Este algoritmo determina cómo el agente elige su próxima acción. Puede ser reactivo, basado en modelos, basado en objetivos o basado en utilidad, dependiendo de la estrategia del agente.

Actuación: El agente realiza la acción seleccionada en el juego, que en este caso sería elegir entre piedra, papel o tijeras.

Modelo general de agente inteligente:

El modelo general de un agente inteligente se puede representar con los siguientes componentes:

Modelo xeral axente intelixente

En este modelo, la percepción y la memoria se utilizan para recopilar información sobre el entorno y el historial de acciones. La selección de acción utiliza esta información para determinar la próxima acción del agente, que se lleva a cabo mediante la actuación.

Este enfoque permite que el agente tome decisiones informadas basadas en su comprensión del entorno y su experiencia pasada. La implementación de cada componente puede variar según la estrategia específica del agente y los detalles del entorno del juego.

Es importante señalar que, para el juego de "piedra, papel, tijeras", el agente puede utilizar diferentes estrategias de selección de acción, como elegir aleatoriamente, seguir una estrategia fija o adaptarse según el comportamiento del oponente. La elección de la estrategia depende de los objetivos y la complejidad del juego.

## Implementación - Simulando IA

Implementa en Python os compoñentes da estrutura do axente para construir a función axente ou función mapa.

Lee o código contigo en [src](./src/) e os [comentarios ao código](./doc/codigo_RPS_explicado.md).

Modifica a función `get_computer_action()` coa estratexia que consideres máis proveitosa para maximizar o **rendemento** do axente. Recorda que a medida do rendemento vese afectada por diversas consideracións.

Engade os compoñentes software que precises para implementar os compoñentes do tipo de programa axente que deseñaches no epígrafe anterior que, de xeito xeral, se incluen na figura seguinte:

![Table Driven Agent Program](./doc/table_driven_agent_program.png)

Consegue que o código satisfaga os principios **SOLID**, en particular, **SRP** e **OCP** para extender a súa lóxica a diferentes versións do xogo.

## Extensión

Unha vez programado o axente para a versión clásica do RPS, extende o súa lóxica para xogar á versión  [pedra, papel, tesoiras, lagarto, Spock](http://www.samkass.com/theories/RPSSL.html)

## Entrega

Nun proxecto no teu github /gitlab co teu código e a documentación, esta última recollida no `README` do proxecto e escrita en formato Markdown.

## Bibliografía

Lutz, Mark. _Learning Python_. Sebastopol, Ca, O’reilly, 2018.

Martin, Robert C. _Clean Code a Handbook of Agile Software Craftmanship_. Upper Saddle River [Etc.] Prentice Hall, 2010.

Martin, Robert C. _Clean Architecture: A Craftsman’s Guide to Software Structure and Design_. Prentice Hall, 2018.

S. McConnel. _Code Complete: A Practical Handbook of Software Construction_, 2dn Edition. Microsoft Press, 2004.

Russell, Peter. _ARTIFICIAL INTELLIGENCE : A Modern Approach_, Global Edition. S.L., Pearson Education Limited, 2021.

‌
