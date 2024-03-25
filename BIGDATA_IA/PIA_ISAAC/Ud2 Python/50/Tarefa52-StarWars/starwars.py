""" 
     por un lado temos os seres biolóxicos: que teñen as seguintes caracteristicas: 
     
     name, height, mass, hair_color, skin_color, eye_color, birth_year, sex, gender, homeworld, species, films
     por outro teremos os droides, que teñen as seguintes características: 
     
     name, height, mass,  birth_year, gender, homeworld,  films

     en comun : 
     name
     height
     mass
     birth_year
     gender
     homeworld
     films

     crear una clase con estas caracteristicas
     """

import csv
from dataclasses import dataclass, field
from typing import List

@dataclass
class PersonajeStarWars:
    name: str
    height: int = None
    mass: int = None
    birth_year: float = None
    gender: str = None
    homeworld: str = None
    films: List[str] = field(default_factory=list)

    def __str__(self):
        return f"Nombre: {self.name}, Altura: {self.height}, Masa: {self.mass}, Año de nacimiento: {self.birth_year}, Género: {self.gender}, Planeta de origen: {self.homeworld}, Películas: {', '.join(self.films)}"

@dataclass
class Biologico(PersonajeStarWars):
    hair_color: str = None
    skin_color: str = None
    eye_color: str = None
    sex: str = None
    species: str = None

    def __str__(self):
        return super().__str__() + f", Color de pelo: {self.hair_color}, Color de piel: {self.skin_color}, Color de ojos: {self.eye_color}, Sexo: {self.sex}, Especie: {self.species}"

@dataclass
class Droide(PersonajeStarWars):
    pass

# Lista para almacenar instancias de ambas clases
personajes_star_wars = []

# Ruta al archivo CSV
archivo_csv = '/media/DIURNO/CURSO/PIA_ISAAC/Ud2 Python/TarefazPIA/Tarefa52-StarWars/starwars.csv'

try:
    # Leer datos desde el archivo CSV y crear instancias de las clases
    with open(archivo_csv, 'r', newline='', encoding='utf-8') as file:
        lector_csv = csv.DictReader(file, delimiter=',')
        for fila in lector_csv:
            try:
                if 'species' in fila:
                    personaje = Biologico(**fila, films=fila['films'].split(','))
                else:
                    personaje = Droide(**fila, films=fila['films'].split(','))
                personajes_star_wars.append(personaje)
            except Exception as e:
                print(f"Error al crear instancia: {e}, Fila: {fila}")

    # Imprimir el conjunto completo de personajes
    for personaje in personajes_star_wars:
        print(personaje)

    # Imprimir solo los personajes que no son droides
    for personaje in personajes_star_wars:
        if isinstance(personaje, Biologico):
            print(personaje)

except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo {archivo_csv}")
except Exception as e:
    print(f"Error inesperado: {e}")