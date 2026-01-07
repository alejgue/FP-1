from got import *
from pathlib import Path

def test_lee_batallas(ruta: Path):
    print("testeando la funcion lee_batallas")
    batalla = lee_batallas(ruta)
    print(f"Leidos {len(batalla)} registros")
    print(f"Los tres primeros son: {batalla[:3]}\n\n")

def test_reyes_mayor_menor_ejercito(batallas: list[BatallaGOT]):
    print("testeando la funcion test_reyes_mayor_menor_ejercito")
    rey_mayor_menor = reyes_mayor_menor_ejercito(batallas)
    print(f"Los reyes con mayor y menor son: {rey_mayor_menor}\n\n")

def test_batallas_mas_comandantes(batallas: list[BatallaGOT], regiones: set[str]| None = None, n: int| None = None):
    print("testeando la funcion test_batallas_mas_comandantes")
    batallas_mas_comand= batallas_mas_comandantes(batallas,regiones,n)
    print(f"Las batallas con mas comandantes son: {batallas_mas_comand}\n\n")

def test_rey_mas_victorias(batallas: list[BatallaGOT], rol: str = "ambos"):
    print("testeando la funcion test_rey_mas_victorias")
    rey_mas_v= rey_mas_victorias(batallas,rol)
    print(f"El rey con mas victorias es: {rey_mas_v}\n\n")

def test_rey_mas_victorias_por_region(batallas: list[BatallaGOT], rol: str = "ambos"):
    print("testeando la funcion test_rey_mas_victorias_por_region")
    rey_mas_vregion= rey_mas_victorias_por_region(batallas,rol)
    print(f"Los reyes con mas victorias por region son: {rey_mas_vregion}\n\n")

def main():
    ruta = Path("Profesor-parte-1/LAB-GameOfThrones-main/data/battles.csv")
    fichero = lee_batallas(ruta)
    
    test_lee_batallas(ruta)
    test_reyes_mayor_menor_ejercito(fichero)
    test_batallas_mas_comandantes(fichero,None,3)
    test_rey_mas_victorias(fichero,"ambos")
    test_rey_mas_victorias_por_region(fichero,"ambos")


if __name__ == "__main__":
    main()