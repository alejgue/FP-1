from typing import NamedTuple, List
from datetime import datetime, date, time
import csv

Vuelo = NamedTuple("Vuelo",
    [("operador", str), # Compañía aérea que operaba el vuelo (opcional)
    ("codigo", str), # Código de vuelo (opcional)
    ("ruta", str), # Ruta del vuelo (opcional)
    ("modelo", str)]) # Modelo de avión que operaba el vuelo (opcional)

Desastre = NamedTuple("Desastre",
    [("fecha", date), # Fecha del desastre aéreo
    ("hora", time | None), # Hora del desastre (opcional)
    ("localizacion", str), # Localización del desastre
    ("supervivientes",int), # Supervivientes
    ("fallecidos",int), # Fallecidos
    ("fallecidos_en_tierra",int), # Fallecidos en tierra (no eran pasajeros del vuelo)
    ("operacion",str), # Momento operativo del vuelo cuando ocurrió el desastre
    ("vuelos", list[Vuelo])]) # Vuelos implicados en el desastre

def lee_desastres(ruta:str)->list[Desastre]:
    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        desastres = []
        for fila in lector:
            fecha = parsea_fecha(fila[0])
            hora = parsea_hora(fila[1]) 
            localizacion = fila[2]
            vuelos = parsea_vuelos(fila[3], fila[4], fila[5], fila[6])
            supervivientes = int(fila[7])
            fallecidos = int(fila[8])
            fallecidos_en_tierra =int(fila[9])
            operacion = fila[6]
            desastres.append(Desastre(fecha, hora, localizacion, supervivientes, fallecidos, fallecidos_en_tierra, operacion, vuelos))
    return desastres

def parsea_fecha(fecha:str) -> date:
    return datetime.strptime(fecha, "%d/%m/%Y").date()

def parsea_hora(hora:str) -> time:
    if not hora:
        return None
    return datetime.strptime(hora, "%H:%M").time()

def parsea_vuelos(operadores:str, codigos:str, rutas:str, modelos:str ) -> List[Vuelo]:
    vuelos = []
    ops=operadores.split("/")
    cds=codigos.split("/")
    ruts= rutas.split("/")
    mdls= modelos.split("/")

    for i in range(len(ops)):
        vuelos.append(Vuelo(operador=ops[i].strip(), codigo=cds[i].strip(), ruta=ruts[i].strip(), modelo=mdls[i].strip()))
    return vuelos

def desastres_con_fallecidos_en_tierra(desastres:list[Desastre],n:int|None=None) -> list[tuple[str,date,time,int]]:
    resultado = []
    for desastre in desastres:
        if desastre.fallecidos_en_tierra > 0:
            resultado.append((desastre.localizacion, desastre.fecha, desastre.hora, desastre.fallecidos_en_tierra))
    resultado.sort(key=lambda x: x[3], reverse=True)
    if n is not None:
        return resultado[:n]
    return resultado