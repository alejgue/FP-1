import csv
from typing import NamedTuple, Counter
from pathlib import Path

RegistroExtranjeria = NamedTuple(
    "RegistroExtranjeria", 
            [("distrito",str),
             ("seccion", str),
             ("barrio", str),
             ("pais",str),
             ("hombres", int),
             ("mujeres", int)
            ]
)

def lee_datos_extranjeria(ruta_fichero: Path) -> list[tuple]:

    lista = []
    with open(ruta_fichero, 'r', encoding="utf-8") as fichero:
        lector = csv.reader(fichero)
        next(lector)
        for linea in lector:
            lista.append(RegistroExtranjeria (
                distrito=linea[0],
                seccion= linea[1],
                barrio= linea[2],
                pais= linea[3],
                hombres= linea[4],
                mujeres= linea[5]
            ))

    return lista


def numero_nacionalidades_distintas(registros: list[RegistroExtranjeria]) -> int:

    coleccion_paises = set()

    for linea in registros:
        coleccion_paises.add(linea.pais)
    
    return len(coleccion_paises)


def secciones_distritos_con_extranjeros_nacionalidades(registros: list[RegistroExtranjeria],  paises: set[str]) -> list[tuple]:
    
    conjunto = set()
    paises_lower = set(pais.lower() for pais in paises)

    for linea in registros:
        if linea.pais.lower() in paises_lower:
            conjunto.add((linea.distrito, linea.seccion))
    
    return sorted(list(conjunto))

def total_extranjeros_por_pais(registros: list[RegistroExtranjeria]) -> dict[str, int]:

    diccionario = dict()


    for linea in registros:
        n_extran = int(linea.hombres + linea. mujeres)
        diccionario[linea.pais] = diccionario.get(linea.pais, 0) + n_extran
    
    return diccionario

def top_n_extranjeria(registros: list[RegistroExtranjeria],  n=3) -> list[tuple]:
    
    diccionario = dict()


    for linea in registros:
        n_extran = int(linea.hombres + linea. mujeres)
        diccionario[linea.pais] = diccionario.get(linea.pais, 0) + n_extran
    
    top_total = sorted(diccionario.items(), key=lambda a: a[1], reverse=True)

    return top_total[:n]


def barrio_mas_multicultural(registros: list[RegistroExtranjeria]) -> str:
    
    barrios_y_paises = {}

    for linea in registros:
        if linea.barrio not in barrios_y_paises:
            barrios_y_paises[linea.barrio] = set()
        
        barrios_y_paises[linea.barrio].add(linea.pais)

    barrio_ganador = max(barrios_y_paises, key=lambda barrio: len(barrios_y_paises[barrio]))

    return barrio_ganador


def barrio_con_mas_extranjeros(registros: list[RegistroExtranjeria], tipo=None) -> str:
    
    tipos = [None, "Hombres", "Mujeres"]
    diccionario = {}

    if tipo not in tipos:
        raise ValueError("El tipo debe de ser 'None', 'Mujeres' o 'Hombres'")
    
    for linea in registros:
        if tipo == None or tipo == "Mujeres":
            diccionario[linea.barrio] = diccionario.get(linea.barrio, 0) + int(linea.mujeres)

        if tipo == None or tipo == "Hombres":
            diccionario[linea.barrio] = diccionario.get(linea.barrio, 0) + int(linea.hombres)

    return max(diccionario, key=diccionario.get)

def pais_mas_representado_por_distrito(registros: list[RegistroExtranjeria]) -> dict[str, str]:
    
    diccionario = {}

    for linea in registros:
        if linea.distrito not in diccionario:
            diccionario[linea.distrito] = Counter()    
        
        total_personas = int(linea.hombres) + int(linea.mujeres)
        diccionario[linea.distrito][linea.pais] += total_personas 

    diccionario_final = {}

    for distrito, pais in diccionario.items():
       diccionario_final[distrito] = max(pais, key= pais.get)

    return diccionario_final

    #valor es PAIS donde hay mas extranjeros residentes en el distrito
    # Hay que sumar SI o SI
def main():
    ruta = Path("Profesor-parte-1/LAB-Extrajeria-main/data/extranjeriaSevilla.csv")
    fichero = lee_datos_extranjeria(ruta)

if __name__ == "__main__":
    main()