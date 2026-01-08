from typing import NamedTuple 
from collections import Counter
from datetime import datetime,date 
from pathlib import Path
import csv

Mejora = NamedTuple("Mejora", 
                    [("denominacion", str), 
                     ("coste", int), 
                     ("fecha", date)]) 

Vivienda = NamedTuple("Vivienda", 
                      [("propietario", str), 
                       ("calle", str), 
                       ("fecha_adquisicion", date), 
                       ("numero", int), 
                       ("metros",float), 
                       ("precio",int), 
                       ("mejoras", list[Mejora])])

def parse_fecha(fecha: str) -> date:
    return datetime.strptime(fecha, "%d/%m/%Y").date()
    
def parsea_mejoras(mejoras_str:str) -> list[Mejora]:
    if not mejoras_str or mejoras_str.strip() == "":
        return []
    
    mejoras_split = mejoras_str.split('*')

    lista_mejoras = []

    for mejoras in mejoras_split:
        caracteristica = mejoras.split('-')
        lista_mejoras.append(Mejora(
            denominacion= caracteristica[0],
            coste= int(caracteristica[1]), 
            fecha= parse_fecha(caracteristica[2])
        ))

    return lista_mejoras


def lee_viviendas(ruta: str) -> list[Vivienda]:

    lista = []

    with open(ruta, 'r', encoding='utf-8') as fichero:
        lector = csv.reader(fichero, delimiter=";")
        next(lector)

        for linea in lector:
            
            lista.append(Vivienda(
                propietario= linea[0],
                calle= linea[1],
                fecha_adquisicion= parse_fecha(linea[3]),
                numero= int(linea[2]),
                metros= float(linea[4]),
                precio= int(linea[5]),
                mejoras= parsea_mejoras(linea[6])
            ))

    return lista


def total_mejoras_por_calle(viviendas: list[Vivienda], par_impar: str) -> dict[str,int]:

    if par_impar is None or par_impar.upper() not in ['PAR', 'IMPAR']:
        raise ValueError("Debe de introducir 'PAR' o 'IMPAR'")

    diccionario = {}

    for linea in viviendas:
        numero_mejoras = len(linea.mejoras)    

        if linea.numero % 2 == 0 and par_impar.upper() == "PAR":
            diccionario[linea.calle] = diccionario.get(linea.calle, 0)+ numero_mejoras
        elif linea.numero % 2 != 0 and par_impar.upper() == "IMPAR":
            diccionario[linea.calle] = diccionario.get(linea.calle, 0)+ numero_mejoras

    return diccionario


def vivienda_con_mejora_mas_rapida(viviendas: list[Vivienda]) -> tuple[str,str,int,int,str]:

    nombre_propietario= None
    calle = None
    numero = None
    dias_desde_mejora = float('inf')
    nombre_mejora = None

    for linea in viviendas:
        if not linea.mejoras:
            continue

        for mejora in linea.mejoras:
           dias_entre_dos = int((mejora.fecha-linea.fecha_adquisicion).days)
           if dias_entre_dos < dias_desde_mejora:
               dias_desde_mejora = dias_entre_dos
               nombre_propietario = linea.propietario
               calle = linea.calle
               numero = int(linea.numero)
               nombre_mejora = mejora.denominacion

    return (nombre_propietario, calle, numero, dias_desde_mejora, nombre_mejora)


def calle_mayor_diferencia_precios(viviendas: list[Vivienda]) -> str:

    dif_precio = 0
    nombre_calle = None

    diccionario = {}

    for linea in viviendas:
        if linea.calle not in diccionario:
            diccionario[linea.calle] = Counter()

        if linea.numero % 2 == 0:
            diccionario[linea.calle]["par"] += linea.precio
        if linea.numero % 2 != 0:
            diccionario[linea.calle]["impar"] += linea.precio
    
    for calle, paridad in diccionario.items():
       diferencia = abs(paridad["par"] - paridad["impar"])

       if diferencia > dif_precio:
         dif_precio = diferencia
         nombre_calle = calle

    return nombre_calle


def n_viviendas_top_valoradas_por_calle(viviendas: list[Vivienda], 
                fecha: date|None = None, n: int = 3) -> dict[str,list[tuple[str,int,int]]]:
    
    diccionario = {}

    for linea in viviendas:
        if linea.calle not in diccionario:
            diccionario[linea.calle] = []
        
        if fecha is None or linea.fecha_adquisicion > fecha:
            dueno = linea.propietario
            numero = linea.numero
            valor = linea.precio + sum(m.coste for m in linea.mejoras)
            #Otra forma
            #valor = linea.precio
            #for mejora in linea.mejoras:
            #    valor += mejora.coste

            diccionario[linea.calle].append((dueno,numero,valor))

    resultado = {}
    for calle, lista_viviendas in diccionario.items():
        # Ordenamos por el tercer elemento de la tupla (valor_total) -> índice 2
        lista_ordenada = sorted(lista_viviendas, key=lambda x: x[2], reverse=True)
        # Guardamos solo las n mejores
        resultado[calle] = lista_ordenada[:n]

    return resultado


def valor_metro_cuadrado_por_calle_y_año(viviendas: list[Vivienda]) -> list[tuple[int,list[tuple[str,float]]]]:
    
    diccionario = {}

    for linea in viviendas:
        ano = linea.fecha_adquisicion.year
        precio_metro = float(linea.precio / linea.metros)
        
        # 1. Si el año no está, creamos un diccionario para ese año
        if ano not in diccionario:
            diccionario[ano] = {}

        # 2. Si la calle no está en ese año, inicializamos [suma, contador]
        if linea.calle not in diccionario[ano]:
            diccionario[ano][linea.calle] = [0.0, 0]
        
        diccionario[ano][linea.calle][0] += precio_metro
        diccionario[ano][linea.calle][1] += 1

    lista = []

    anos_ordenados = sorted(diccionario.keys())

    for ano in anos_ordenados:
        lista_calles_del_ano = []
        
        for calle, datos in diccionario[ano].items():
            promedio = datos[0] / datos[1]
            lista_calles_del_ano.append((calle, promedio))
        
        # Ordenamos las calles por precio de mayor a menor (Requisito 2)
        # x[1] es el precio promedio en la tupla (calle, promedio)
        lista_calles_del_ano.sort(key=lambda x: x[1], reverse=True)
        
        # Añadimos al resultado final la tupla (año, lista_de_calles_ordenada)
        lista.append((ano, lista_calles_del_ano))

    return lista



