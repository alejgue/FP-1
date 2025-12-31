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

def leer_batallas(ruta: Path) -> list[BatallaGOT]:
    batallas = []
    with open(ruta, "r", encoding="utf-8") as fichero:
        lector = csv.reader(fichero, delimiter=",")
        next(lector)  # Saltar la cabecera
        for linea in lector:
            name = linea[0]
            attacker_king = linea[1]
            defender_king = linea[2]
            attacker_outcome = linea[3].lower() == "win"
            major_death = linea[4].lower() == "1"
            attacker_commander = linea[5].split(", ") if linea[5]  else []
            defender_commander= linea[6].split(", ")  if linea[6]  else []
            region= linea[7]
            attacker_size= int(linea[8]) if linea[8] else None
            defender_size= int(linea[9]) if linea[9] else None

            batalla= BatallaGOT(name, attacker_king, defender_king,attacker_outcome, major_death, attacker_commander, defender_commander, region, attacker_size, defender_size)
            batallas.append(batalla)
    return batallas


if __name__ == '__main__':
    ruta= Path('data/battles.csv')
    print(leer_batallas(ruta))