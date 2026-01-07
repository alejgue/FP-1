import csv
from pathlib import Path
from typing import NamedTuple, Counter

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

def lee_batallas(ruta: Path) -> list[tuple]:
    
    batallas = []
    
    with open(ruta, 'r', encoding="UTF-8") as fichero:
      lector = csv.reader(fichero)
      next(lector)
      
      for linea in lector:
         batallas.append(BatallaGOT (
            nombre= linea[0],
            rey_atacante= linea[1],
            rey_atacado= linea[2],
            gana_atacante= True if linea[3].lower() == "win" else False,
            muertes_principales= bool(linea[4]),
            comandantes_atacantes= linea[5].split(", ") if linea[5]  else [],
            comandantes_atacados= linea[6].split(", ") if linea[6]  else [],
            region = linea[7],
            num_atacantes= int(linea[8]) if linea[8] else None,
            num_atacados= int(linea[9]) if linea[9] else None
         ))
    
    return batallas

def reyes_mayor_menor_ejercito(batallas: list[BatallaGOT]) -> tuple[str, str]:
    
    diccionario = {}

    for linea in batallas:
      
      atacante = linea.rey_atacante
      ejercito_atacante = linea.num_atacantes
      atacado = linea.rey_atacado
      ejercito_atacado = linea.num_atacados
      
      if atacante not in diccionario:
         diccionario[atacante] = 0
      
      if atacado not in diccionario:
         diccionario[atacado] = 0
      
      diccionario[atacante] += ejercito_atacante or 0
      diccionario[atacado] += ejercito_atacado or 0

    nombre_rey_max = max(diccionario, key=diccionario.get)
    nombre_rey_min = min(diccionario, key=diccionario.get)

    return (f"rey mayor ejercito: {nombre_rey_max}", f"rey menor ejercito: {nombre_rey_min}")


def batallas_mas_comandantes(batallas: list[BatallaGOT], regiones: set[str]| None = None, n: int| None = None) -> list[tuple[str, int]]:
    
    lista = list()

    for linea in batallas:
        
        if regiones is None or linea.region in regiones:
            total_comandantes = len(linea.comandantes_atacados) + len(linea.comandantes_atacantes)
            tupla = (linea.nombre, total_comandantes)
            lista.append(tupla)
    
    lista.sort(key=lambda a: a[1], reverse=True) #modifica directamente la lista original
    return lista[:n]     

    #Otra forma (crea otra lista)
    #return sorted(lista, key=lambda a: a[1], reverse=True)[:n]


def rey_mas_victorias(batallas: list[BatallaGOT], rol: str = "ambos") -> str | None:

    roles_validos = ["atacante", "atacado", "ambos", None]
    if rol not in roles_validos:
        raise ValueError("Solo se admite 'atacante', 'atacado' o 'ambos'")

    diccionario = {}

    for batalla in batallas:
      
        if rol in ["atacante", "ambos", None]:
            if batalla.gana_atacante is True and batalla.rey_atacante:
                rey = batalla.rey_atacante
                diccionario[rey] = diccionario.get(rey, 0) + 1
        
        if rol in ["atacado", "ambos", None]:
            if batalla.gana_atacante is False and batalla.rey_atacado:
                rey = batalla.rey_atacado
                diccionario[rey] = diccionario.get(rey, 0) + 1

    if not diccionario:
        return None

    return max(diccionario, key=diccionario.get)


def rey_mas_victorias_por_region(batallas: list[BatallaGOT], rol: str = "ambos") -> dict[str, tuple[str, int]]:
    
    roles_validos = ["atacante", "atacado", "ambos", None]
    if rol not in roles_validos:
        raise ValueError("Solo se admite 'atacante', 'atacado' o 'ambos'")

    diccionario = {}

    for batalla in batallas:
      
        if rol in ["atacante", "ambos", None]:
            if batalla.gana_atacante is True and batalla.rey_atacante:
                rey, region = batalla.rey_atacante, batalla.region
                
                if region not in diccionario:
                    diccionario[region] = Counter()

                diccionario[region][rey] += 1

        
        if rol in ["atacado", "ambos", None]:
            if batalla.gana_atacante is False and batalla.rey_atacado:
                rey, region = batalla.rey_atacado, batalla.region
                
                if region not in diccionario:
                    diccionario[region] = Counter()

                diccionario[region][rey] += 1

    if not diccionario:
        return {}

    resultado_final = {}

    for region, conteo in diccionario.items():
        top_winner_region = max(conteo, key= conteo.get)
        resultado_final[region] = (top_winner_region, conteo[top_winner_region])
 
    return resultado_final
    
    
def main():
    ruta = Path("Profesor-parte-1/LAB-GameOfThrones-main/data/battles.csv")
    fichero = lee_batallas(ruta)
    #print(reyes_mayor_menor_ejercito(fichero))
    #print(batallas_mas_comandantes(fichero,None,3))
    #print(rey_mas_victorias(fichero,"ambos"))
    print(rey_mas_victorias_por_region(fichero,"ambos"))


if __name__ == "__main__":
    main()