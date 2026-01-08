from typing import NamedTuple 
from collections import Counter, defaultdict
from datetime import date, datetime
import csv

Suscripcion = NamedTuple("Suscripcion", 
                         [("nombre", str), 
                          ("dni", str), 
                          ("fecha_inicio", date), 
                          ("fecha_fin", date | None), # Será None si la suscripción sigue activa 
                          ("tipo_plan", str), 
                          ("num_perfiles", int), 
                          ("precio_mensual", float), 
                          ("addons", list[str]) ])

def parse_fecha(fecha: str) -> date:
   return datetime.strptime(fecha, "%Y-%m-%d").date()

def lee_suscripciones(ruta_fichero: str) -> list[Suscripcion]:
    
    lista = []

    with open(ruta_fichero, 'r', encoding='utf-8') as fichero:
        lector = csv.reader(fichero)
        next(lector)
        
        for linea in lector:
            ads = [a.strip() for a in linea[7].split(",")] if linea[7] else []

            lista.append(Suscripcion(
                nombre=linea[0],
                dni= linea[1],
                fecha_inicio= parse_fecha(linea[2]),
                fecha_fin= parse_fecha(linea[3]) if linea[3] else None,
                tipo_plan= linea[4],
                num_perfiles= int(linea[5]),
                precio_mensual= float(linea[6]),
                addons= ads
            )) 

    return lista


def suscripciones_mas_rentables(suscripciones: list[Suscripcion], n: int = 3, 
                                tipos_plan: set[str]|None = None) -> list[tuple[str, float]]:

    lista = []

    for linea in suscripciones:
        
        if tipos_plan is None or linea.tipo_plan in tipos_plan:
            precio_diario = float(linea.precio_mensual / 30)
            fecha_fin = linea.fecha_fin

            if not fecha_fin:
                fecha_fin = date.today()

            total_dias = (fecha_fin - linea.fecha_inicio).days 
            importe_total = float(precio_diario * total_dias)
            lista.append((linea.dni, importe_total))
            
    lista_sorteada = sorted(lista, key= lambda a: a[1], reverse=True)
    
    return lista_sorteada[:n] 

def plan_mas_perfiles(suscripciones: list[Suscripcion], 
                      fecha_ini: date|None = None, fecha_fin: date|None = None) -> tuple[str, int]:
    #tupla(tipo_plan, total perfiles) que tiene mayor numero total perfiles

    suscripciones_ordenadas = sorted(suscripciones, key= lambda a: a.fecha_inicio)

    diccionario = dict()

    for linea in suscripciones_ordenadas:
        if fecha_ini is None or linea.fecha_inicio >= fecha_ini:
            if fecha_fin is None or linea.fecha_fin <= fecha_fin:

                diccionario[linea.tipo_plan] = diccionario.get(linea.tipo_plan, 0) + linea.num_perfiles

    max_diccionario_valor = max(diccionario.values())
    max_diccionario_nombre = max(diccionario, key=diccionario.get)

    return (max_diccionario_nombre,max_diccionario_valor)


def media_dias_por_plan(suscripciones: list[Suscripcion]) -> dict[str, float]:

    suscripciones_ordenadas = sorted(suscripciones, key= lambda a: a.fecha_inicio)

    diccionario = {}

    for linea in suscripciones_ordenadas:
        if linea.fecha_fin:
            dias = (linea.fecha_fin - linea.fecha_inicio).days

            if linea.tipo_plan not in diccionario:
                diccionario[linea.tipo_plan] = [0.0, 0]
            
            diccionario[linea.tipo_plan][0] += dias
            diccionario[linea.tipo_plan][1] += 1

    diccionario_resultante = {}

    for tipo_plan, datos in diccionario.items():
        media_dias = datos[0] / datos[1]
        print(media_dias)
        diccionario_resultante[tipo_plan] = diccionario_resultante.get(tipo_plan, 0.0) + media_dias

    return diccionario_resultante


def addon_mas_popular_por_año(suscripciones: list[Suscripcion]) -> dict[int,str]:
 #Devuelve un diccionario que hace corresponder a cada año de inicio 
 #de suscripción el addon que aparece en más suscripciones ese año.

    suscripciones_ordenadas = sorted(suscripciones, key= lambda a: a.fecha_inicio)

    diccionario = {}

    for linea in suscripciones_ordenadas:

        ano = linea.fecha_inicio.year

        if ano not in diccionario:
            diccionario[ano] = Counter()

        for addon in linea.addons:
            diccionario[ano][addon] += 1 

    diccionario_resultante = defaultdict(str)

    for ano, addon in diccionario.items():
        addon_popular = max(addon, key=addon.get)

        diccionario_resultante[ano] = addon_popular

    return diccionario_resultante


def evolucion_años(suscripciones: list[Suscripcion]) -> list[tuple[int, int]]:
    # 1. Contamos variaciones netas por año (+1 inicio, -1 fin) 
    neto_por_año = defaultdict(int)
    for s in suscripciones:
        neto_por_año[s.fecha_inicio.year] += 1 
        if s.fecha_fin:
            neto_por_año[s.fecha_fin.year] -= 1 

    # 2. Ordenamos años y calculamos la diferencia entre ellos 
    años_ordenados = sorted(neto_por_año.items()) 
    evolucion = []
    for (a1, v1), (a2, v2) in zip(años_ordenados, años_ordenados[1:]): 
       evolucion.append((a2, v2 - v1)) 
    return evolucion

# fin de la suscripción (la fecha de fin puede estar vacía, 
# en cuyo caso se supone que la suscripción sigue activa)

# Si una suscripción no tiene addons, se almacenará una lista vacía en la tupla correspondiente.

# Para calcular el importe total de una suscripción, se considera 
# un precio diario igual al precio mensual dividido entre 30.
#El importe total se calculará multiplicando el precio diario por el total de días de la suscripción.