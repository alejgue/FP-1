from collections import namedtuple
import csv
from datetime import datetime

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(fichero: str) -> list[Entreno]:
    '''recibe el nombre de un fichero de texto con los datos de los entrenamientos y devuelve una lista de tuplas de tipo Entreno.
    '''
    entrenos = []
    with open(fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)  # Saltar la cabecera
        for fila in lector:
            tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido = fila
            entreno = Entreno(
                tipo=tipo,
                fechahora=datetime.strptime(fechahora,"%d/%m/%Y %H:%M"),
                ubicacion=ubicacion,
                duracion=int(duracion),
                calorias=int(calorias),
                distancia=float(distancia),
                frecuencia=int(frecuencia),
                compartido=compartido
                )
            entrenos.append(entreno)
    return entrenos

def tipos_entreno(entrenos: list[Entreno]) -> list[str]:
    '''recibe una lista de tuplas de tipo Entreno, y devuelve una lista con todos los tipos de entrenamientos en orden alfabético y sin repetir ninguno.
    '''
    return sorted(set(entreno.tipo for entreno in entrenos))

def entrenos_duracion_superior(entrenos: list[Entreno], d: int) -> list[Entreno]:
    '''recibe una lista de tuplas de tipo Entreno y un valor entero d, y devuelve una lista con todos los entrenamientos que tienen una duración superior
    al valor d.
    '''
    return [entreno for entreno in entrenos if entreno.duracion > d]

def suma_calorias(entrenos: list[Entreno], f_inicio, f_fin) -> int:
    '''recibe una lista de tuplas de tipo Entreno y dos fechas, de tipo `datetime`, f_inicio y f_fin, y devuelve la suma de las calorías quemadas en todos los entrenamientos realizados entre las dos fechas f_inicio y f_fin, ambas incluidas.
    '''
    resultado = 0
    for entreno in entrenos:
        if f_inicio <= entreno.fechahora <= f_fin:
            resultado += entreno.calorias
    return resultado


def entrenamiento_mas_kms(entrenos: list[Entreno]) -> Entreno:
    '''recibe una lista de tuplas de tipo Entreno y devuelve el entrenamiento en el que se han recorrido más kilómetros.
    '''
    entrenoMax = None
    for entreno in entrenos:
        if entrenoMax is None or entreno.distancia > entrenoMax.distancia:
            entrenoMax = entreno
    return entrenoMax

def duracion_media_entrenos(entrenos: list[Entreno], anio: int, mes: int) -> float | None:
    duracion_suma = 0
    elementos=0

    f_inicio = datetime(anio, mes, 1)
    f_fin =datetime(anio, mes, 30) 

    for entreno in entrenos:
        if f_inicio <= entreno.fechahora <= f_fin:
            duracion_suma += entreno.duracion
            elementos += 1

    if elementos == 0:
        return None
    return duracion_suma / elementos


if __name__ == '__main__':
    entrenos = lee_entrenos('data/entrenos.csv')
    #print(entrenos)
    #print(tipos_entreno(entrenos))
    #print(entrenos_duracion_superior(entrenos, 30))
    resultado = suma_calorias(entrenos, datetime(2019,1,1), datetime(2021,12,31))
    print(resultado)