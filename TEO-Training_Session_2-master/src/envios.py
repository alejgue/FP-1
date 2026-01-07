from __future__ import annotations

from datetime import date, datetime
from typing import NamedTuple, Counter
import csv


class Envio(NamedTuple):
    id_envio: str
    cliente: str
    fecha_salida: date
    fecha_entrega: date
    origen: str
    destino: str
    transporte: str
    prioridad: str
    segmento: str
    peso_kg: float
    coste: float


class Incidencia(NamedTuple):
    id_envio: str
    tipo: str
    descripcion: str
    dias_retraso: int
    compensacion: float


MESES = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}


def parse_fecha(cadena: str) -> date:
    """Convierte fecha ISO (YYYY-MM-DD) a date."""
    return datetime.strptime(cadena, "%Y-%m-%d").date()


def lee_envios(ruta: str) -> list[Envio]:
    """Lee el CSV de envíos."""
    
    dict = []
    
    with open(ruta, 'r', encoding='utf-8') as fichero:
        
        lector = csv.reader(fichero)
        next(lector)
        
        for linea in lector:
            dict.append(Envio(
                id_envio= linea[0],
                cliente= linea[1],
                fecha_salida= parse_fecha(linea[2]),
                fecha_entrega= parse_fecha(linea[3]),
                origen= linea[4],
                destino= linea[5],
                transporte= linea[6],
                prioridad= linea[7],
                segmento= linea[8],
                peso_kg= float(linea[9]),
                coste= float(linea[10])
            ))
    
    return dict
    

def lee_incidencias(ruta: str) -> list[Incidencia]:
    """Lee el CSV de incidencias."""
    
    dict = []
    
    with open(ruta, 'r', encoding='utf-8') as fichero:
        
        lector = csv.reader(fichero)
        next(lector)
        
        for linea in lector:
            dict.append(Incidencia(
                 id_envio = linea[0],
                 tipo = linea[1],
                 descripcion = linea[2],
                 dias_retraso = int(linea[3]),
                 compensacion = float(linea[4])
            ))
    
    return dict


def coste_total(
    envios: list[Envio],
    cliente: str | None = None,
    prioridades: set[str] | None = None,
) -> float:
    """Suma el coste total aplicando filtros opcionales."""
    
    prioridades_validas = ['ALTA', 'MEDIA', 'BAJA']
    p_filtro = set()

    if prioridades is not None:
        p_filtro = {p.upper() for p in prioridades}  #lista
        if not p_filtro.issubset(prioridades_validas): # issubset es de listas
            raise ValueError("Las prioridades deben ser 'ALTA', 'MEDIA' o 'BAJA'")
        
    coste_total = 0.0

    for linea in envios:
        
        filtro_cliente = (cliente is None or linea.cliente == cliente)
        filtro_prioridad = (prioridades is None or linea.prioridad.upper() in p_filtro)

        if filtro_cliente and filtro_prioridad:
            coste_total += linea.coste
    
    return coste_total


def destinos_top_por_peso(
    envios: list[Envio],
    transporte: str | None = None,
    n: int = 3,
) -> list[tuple[str, float]]:
    """Top-N de destinos según el peso enviado."""
    
    diccionario = {}

    for linea in envios:
        if (transporte is None or linea.transporte == transporte):
            diccionario[linea.destino] = diccionario.get(linea.destino, 0) + float(linea.peso_kg)    
    
    diccionario_sorteado = sorted(diccionario.items(), key=lambda dicci: dicci[1], reverse=True)        
    
    return diccionario_sorteado[:n]


def cliente_con_mas_incidencias(
    envios: list[Envio],
    incidencias: list[Incidencia],
    tipos: set[str] | None = None,
) -> tuple[str, int]:
    """Cliente con mayor número de incidencias (opcionalmente filtradas)."""
    
    tipo = ["DEMORA", "DANO", "PERDIDA"]
    tipos_upper = set() #Por seguridad, no hace falta

    if tipos is not None:
        tipos_upper = {linea.upper() for linea in tipos}
        if not tipos_upper.issubset(tipo):
            raise ValueError("El tipo debe de ser 'DEMORA', 'DANO', 'PERDIDA'")

    diccionario_envios = {}
    diccionario_incidencias = {}

    for linea in envios:
        diccionario_envios[linea.id_envio] = linea.cliente #Para usar .append creamos la lista primero
    # OTRA FORMA
    # diccionario_envios = {linea.id_envio: linea.cliente for linea in envios}

    for linea in incidencias:
        if tipos is None or linea.tipo.upper() in tipos_upper:
            if linea.id_envio in diccionario_envios.keys(): 
                # Tambien puedo poner 'if nombre_cliente' y comprueba si el ID existe en la lista de envios
                Nombre_cliente = diccionario_envios.get(linea.id_envio)
                diccionario_incidencias[Nombre_cliente] = diccionario_incidencias.get(Nombre_cliente, 0) +1
    
    #En caso de que no haya ninguna incidencia
    if not diccionario_incidencias:
        return ("", 0)

    return max(diccionario_incidencias.items(), key= lambda a: a[1])


def retraso_medio_por_mes(
    envios: list[Envio],
    incidencias: list[Incidencia],
    prioridad: str | None = None,
) -> dict[str, float]:
    """Diccionario mes -> retraso medio en días para esa prioridad."""
    
    # 1. Validación de prioridad
    prioridad_upper = prioridad.upper() if prioridad else None
    if prioridad_upper and prioridad_upper not in ["ALTA", "MEDIA", "BAJA"]:
        raise ValueError("La prioridad debe ser 'ALTA', 'MEDIA' o 'BAJA'")

    # 2. Mapa: ID_envio -> Mes (Solo de los que cumplen la prioridad)
    # Guardamos el mes como string "01", "02", etc.
    id_a_mes = {}
    for linea in envios:
        if prioridad_upper is None or linea.prioridad.upper() == prioridad_upper:
            # Extraemos el mes (suponiendo que fecha_salida es objeto date)
            # El formato :02d asegura que sea "01" en lugar de "1", porque sin el 0, diria que '10' va antes que el '2'
            mes_str = f"{linea.fecha_salida.month:02d}" 
            id_a_mes[linea.id_envio] = mes_str  

    # 3. Acumuladores por mes
    sumas_retraso = {} # mes -> suma total de días
    conteos_retraso = {} # mes -> cuántas incidencias hubo

    for inc in incidencias:
        # ¿Este incidente pertenece a un envío que nos interesa?
        if inc.id_envio in id_a_mes:
            mes = id_a_mes[inc.id_envio]
            retraso = int(inc.dias_retraso)
            
            sumas_retraso[mes] = sumas_retraso.get(mes, 0) + retraso
            conteos_retraso[mes] = conteos_retraso.get(mes, 0) + 1

    resultado = {}
    for mes in sumas_retraso:
        resultado[mes] = sumas_retraso[mes] / conteos_retraso[mes]

    return resultado


def segmento_mas_rentable(
    envios: list[Envio],
    minimo_envios: int = 2,
) -> tuple[str, float]:
    """Segmento con mayor facturación media, restringiendo por nº mínimo de envíos."""

    diccionario_repeticiones = {}
    diccionario_coste = {}

    for linea in envios:
        
        segmento = linea.segmento
        
        diccionario_repeticiones[segmento] = diccionario_repeticiones.get(segmento, 0) + 1
        diccionario_coste[segmento] = diccionario_coste.get(segmento, 0.0) + float(linea.coste)

    diccionario_resultante = {}

    for segmento, n_envios in diccionario_repeticiones.items():
        if n_envios >= minimo_envios:
            diccionario_resultante[segmento] = diccionario_coste[segmento] / n_envios
            # Otra forma (peor)
            #for segmen, coste in diccionario_coste.items():
                #if segmento == segmen:
                    #coste_total = int(coste/n_envios)
                    #diccionario_resultante[segmento] = coste_total 
          
    if not diccionario_resultante: # Buscamos el maximo
        raise ValueError("No hay ningun segmento con tal numero minimo de envios")
    
    return max(diccionario_resultante.items(), key= lambda a: a[1])
    

def dias_medios_entre_envios(
    envios: list[Envio],
    cliente: str | None = None,
) -> float:
    """Media de días entre salidas consecutivas."""
    
    envios_filtrados = [
        linea for linea in envios 
        if cliente is None or linea.cliente == cliente
    ]
    
    # Si hay 0 o 1 envío, no hay "intervalos" entre ellos
    if len(envios_filtrados) < 2:
        return 0.0

    envios_ordenados = sorted(envios_filtrados, key=lambda e: e.fecha_salida)
    
    total_dias = 0
    numero_intervalos = len(envios_ordenados) - 1

    for i in range(1, len(envios_ordenados)):  #con '1' empezamos en el segundo
        actual = envios_ordenados[i].fecha_salida  #Puedo hacerlo sin necesidad del bucle 
        anterior = envios_ordenados[i-1].fecha_salida #poniendo solamente el numero
                                                    #Pero no puedo poner el ID o origen
        diferencia = (actual - anterior).days       # Esto solamente en diccionario
        total_dias += diferencia

    return total_dias / numero_intervalos


if __name__ == "__main__":
    import pathlib

    base = pathlib.Path(__file__).resolve().parent.parent / "data"
    print(base)
