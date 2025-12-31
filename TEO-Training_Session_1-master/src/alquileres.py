from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, datetime
from typing import NamedTuple
import csv


class Alquiler(NamedTuple):
    nombre: str
    dni: str
    fecha_inicio: date
    fecha_fin: date
    estacion: str
    bici_tipo: str
    precio_dia: float
    servicios: list[str]


def parse_fecha(cadena: str) -> date:
    """Convierte una fecha ISO (YYYY-MM-DD) a date."""
    return datetime.strptime(cadena, "%Y-%m-%d").date()


def lee_alquileres(ruta: str) -> list[Alquiler]:
    """Lee el CSV y devuelve una lista de Alquiler."""
    alquileres = []
    with open(ruta, "r", encoding="utf-8") as fichero:
       lector = csv.reader(fichero)
       next(lector)
       for linea in lector:
        alquileres.append(Alquiler(
                nombre=linea[0],
                dni=linea[1],
                fecha_inicio=parse_fecha(linea[2]),
                fecha_fin=parse_fecha(linea[3]),
                estacion=linea[4],
                bici_tipo=linea[5],
                precio_dia=float(linea[6]),
                servicios=linea[7].split(",")
            ))
    return alquileres

def total_facturado(
    alquileres: list[Alquiler],
    fecha_ini: date | None = None,
    fecha_fin: date | None = None,
) -> float:
    """Suma lo cobrado en el rango de fechas (fecha_inicio)."""
    
    total = 0.0

    for linea in alquileres:
        cumple_inicio = (fecha_ini is None or linea.fecha_inicio >= fecha_ini)
        cumple_fin = (fecha_fin is None or linea.fecha_inicio <= fecha_fin)

        if cumple_inicio and cumple_fin:
            dias = (linea.fecha_fin - linea.fecha_inicio).days
            total += dias * linea.precio_dia
            
    return total
    '''
    OTRA FORMA (NO ES LO QUE PIDE ENUINCIADO)
    total = 0.0

    for linea in alquileres:
       if fecha_ini is None or linea.fecha_inicio >= fecha_ini:
            linea_alquiler = (linea.fecha_fin - linea.fecha_inicio).days
            if fecha_fin is None or linea.fecha_fin > fecha_fin:
                linea_alquiler =  (fecha_fin - linea.fecha_inicio).days   
            total += linea_alquiler * linea.precio_dia

    return total
    '''      
           

def alquileres_mas_largos(
    alquileres: list[Alquiler],
    n: int = 3,
) -> list[tuple[str, date]]:
    """Top-N de alquileres más largos (nombre, fecha_inicio). Ordenados mayor a menor"""
    ordenadas = sorted(
        alquileres,
        key=lambda a: (a.fecha_fin - a.fecha_inicio).days,
        reverse=True
    )
    return [(r.nombre, r.fecha_inicio) for r in ordenadas[:n]]


def cliente_mayor_facturacion(
    alquileres: list[Alquiler],
    servicios: set[str] | None = None,
) -> tuple[str, float]:
    """Cliente con mayor gasto opcionalmente filtrando por servicios."""

    gastos_por_cliente = {}

    for linea in alquileres:
        if servicios:
            servicios_alquiler = set(linea.servicios)
            if not servicios.issubset(servicios_alquiler):
                continue
        
        dias = (linea.fecha_fin - linea.fecha_inicio).days
        importe = dias * linea.precio_dia
        gastos_por_cliente[linea.dni] = gastos_por_cliente.get(linea.dni, 0.0) + importe
    
    if not gastos_por_cliente:
        return ("", 0.0)
    
    dni_max = max(gastos_por_cliente, key=gastos_por_cliente.get) #key = criterio de busqueda
    return (dni_max, gastos_por_cliente[dni_max])


def servicio_top_por_mes(
    alquileres: list[Alquiler],
    estaciones: set[str] | None = None,
) -> dict[str, str]:
    """Servicio más contratado por mes (fecha_inicio), filtrando estaciones opcionalmente."""
    
    conteo_mes = {}
    nombres_meses = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }

    for linea in alquileres:
       if estaciones is not None and linea.estacion not in estaciones:
           continue
       
       mes_nombre = nombres_meses[linea.fecha_inicio.month]
       
       if mes_nombre not in conteo_mes:
           conteo_mes[mes_nombre] = Counter() # libreta que meto dentro de cada mes
       
       for s in linea.servicios:
           if s:
               conteo_mes[mes_nombre][s] += 1
   
    resultado_final = {}
    
    for mes, contador in conteo_mes.items():
        top_servicio = max(contador, key=contador.get)
        resultado_final[mes] = top_servicio
    
    return resultado_final


def media_dias_entre_alquileres(alquileres: list[Alquiler]) -> float:
    """Media de días entre alquileres consecutivos (por fecha_inicio)."""
    
    alquileres_ordenados = sorted(alquileres, key=lambda a: a.fecha_inicio)
    
    total_dias = 0
    total_huecos = 0

    for i in range(1, len(alquileres_ordenados)):
        actual = alquileres_ordenados[i].fecha_inicio
        anterior = alquileres_ordenados[i-1].fecha_inicio
        
        total_dias += (actual - anterior).days
        total_huecos += 1

    return total_dias / total_huecos if total_huecos > 0 else 0.0


def indexar_por_estacion(alquileres: list[Alquiler]) -> dict[str, list[Alquiler]]:
    """Diccionario estacion -> lista de Alquiler."""
    diccionario = {}

    for linea in alquileres:
        # Si la clave no existe, crea [] y luego añade el elemento
        diccionario.setdefault(linea.estacion, []).append(linea)
        
        #Lo mismo pero en mas lineas
        #if linea.estacion not in diccionario:
        #    diccionario[linea.estacion] = []
        #diccionario[linea.estacion].append(linea)
    
    return diccionario


if __name__ == "__main__":
    # Espacio para pruebas rápidas
    import pathlib

    ruta = pathlib.Path(__file__).resolve().parent.parent / "data" / "alquileres.csv"
    print(f"Dataset: {ruta}")
