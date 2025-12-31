## Definición de tipos
# Creación de una tupla con nombre para las coordenadas
from typing import NamedTuple
from math import radians, sin, cos, asin, sqrt
Coordenadas = NamedTuple('Coordenadas', [
    ('latitud', float), ('longitud', float)
])

def a_radianes(coordenadas:Coordenadas)->Coordenadas:
    '''Convierte unas coordenadas en grados a radianes

    :param coordenadas: Coordenadas que se quieren convertir a radianes
    :return: Las coordenadas convertidas a radianes
    '''
    pass


def distancia_haversine(coordenadas1:Coordenadas, coordenadas2:Coordenadas)->Coordenadas:
    '''Devuelve la distancia de harvesine entre dos coordenadas

    :param coordenadas1: Coordenadas del primer punto
    :param coordenadas2: Coordenadas del segundo punto
    :return: La distancia harvesine entre las dos coordenadas dadas como parámetro
    '''
    pass

def redondear(coordenadas:Coordenadas)->Coordenadas:
    '''Devuelve unas coordenadas cuya latitud y longitud son 
    el redondeo de la latitud y la longitud de las coordenadas originales

    :param coordenadas: Coordenadas que se quieren convertir a radianes
    :return: Las coordenadas redondeadas
    '''
    pass