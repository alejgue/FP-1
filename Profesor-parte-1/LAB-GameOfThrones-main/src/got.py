from typing import NamedTuple
from pathlib import Path
import csv

BatallaGOT = NamedTuple('BatallaGOT',                         
                        [
                            ('nombre', str),
                            ('rey_atacante', str),
                            ('rey_atacado', str),
                            ('gana_atacante', bool),
                            ('muertes_principales', bool),
                            ('comandantes_atacantes', list[str]),
                            ('comandantes_atacados', list[str]),
                            ('region', str),
                            ('num_atacantes', int|None),
                            ('num_atacados',int|None)
                        ])

def lee_batallas(ruta:str) -> list[tuple]:
    batallas = []
    with open(ruta,"r", encoding="utf-8") as f:
       lector = csv.reader(f)
       next(lector)
       for lineas in lector:
           nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados = lineas
           if num_atacantes is None or num_atacantes == '':
                num_atacantes = 0
           if num_atacados is None or num_atacados == '':
                num_atacados = 0

            #gana_atacante = gana_atacante.lower() == 'true' if isinstance(gana_atacante, str) else bool(gana_atacante)
            #muertes_principales = muertes_principales.lower() == 'true' if isinstance(muertes_principales, str) else bool(muertes_principales)
           batalla = BatallaGOT(
                nombre = str(nombre),
                rey_atacante = str(rey_atacante),
                rey_atacado = str(rey_atacado),
                gana_atacante = bool(gana_atacante),
                muertes_principales = bool(muertes_principales),
                comandantes_atacantes = comandantes_atacantes.strip(),
                comandantes_atacados = comandantes_atacados.strip(),
                region = str(region),
                num_atacantes = int(num_atacantes),
                num_atacados = int(num_atacados)
              )
           batallas.append(batalla)
    return batallas

def reyes_mayor_menor_ejercito(archivo:list[tuple] ) -> tuple[str, str]:
    """
    reyes_mayor_mener_ejerc = []
    reyes = set()
    reyes_con_ejercito = []
    for linea in archivo:
        reyes.add(linea.rey_atacante)
        reyes.add(linea.rey_atacado)
        for rey in reyes:
            total = 0
            if rey in linea.rey_atacante:
                total += linea.num_atacantes
            elif rey in linea.rey_atacado:
                total += linea.num_atacados
        reyes_con_ejercito.append(rey, total)
    print(reyes_con_ejercito)
    """
    ejercitos_por_rey = {}
    for linea in archivo:
        # Sumar ejército del rey atacante
        if linea.rey_atacante:
            ejercitos_por_rey[linea.rey_atacante] = ejercitos_por_rey.get(linea.rey_atacante, 0) + linea.num_atacantes

        # Sumar ejército del rey atacado
        if linea.rey_atacado:
            ejercitos_por_rey[linea.rey_atacado] = ejercitos_por_rey.get(linea.rey_atacado, 0) + linea.num_atacados
                #dame el ejército actual de este rey, o 0 si aún no lo tiene en el diccionario
        # Si no hay datos, devolvemos None
        if not ejercitos_por_rey:
            return (None, None)

    # Buscar el rey con el mayor y menor ejército total
    rey_mayor = max(ejercitos_por_rey, key=ejercitos_por_rey.get)
    rey_menor = min(ejercitos_por_rey, key=ejercitos_por_rey.get)

    return (rey_mayor, rey_menor)
    
def main():
    ruta_archivo = "data//battles.csv"
    archivo = lee_batallas(ruta_archivo)
    print(reyes_mayor_menor_ejercito(archivo))
if __name__ == "__main__":
    main()