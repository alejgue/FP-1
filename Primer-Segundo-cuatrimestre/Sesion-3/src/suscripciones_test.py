from suscripciones import *
from pathlib import Path

def test_lee_suscripciones(ruta_fichero: str):
    print("Test 'lee_carreras'")
    fichero = lee_suscripciones(ruta_fichero)
    print(f"Total suscripciones {len(fichero)}")
    print(f"Las tres primeras: \n {fichero[:3]}")
    print(f"Las tres ultimas: \n {fichero[- 3:]}")
    print("#"*70 + "\n")

def test_suscripciones_mas_rentables(suscripciones: list[Suscripcion], n: int = 3, 
                                tipos_plan: set[str]|None = None):
    print("Test 'lee_carreras'")
    mas_rentables = suscripciones_mas_rentables(suscripciones)
    print(f"Las {n} suscipciones mas rentables filtradas por ({tipos_plan}): \n {mas_rentables}")
    print("#"*70 + "\n")

def test_plan_mas_perfiles(suscripciones: list[Suscripcion], 
                      fecha_ini: date|None = None, fecha_fin: date|None = None):
    print("Test 'plan_mas_perfiles'")
    mas_perfiles = plan_mas_perfiles(suscripciones)
    print(f"El plan con mas perfiles es: {mas_perfiles}")
    print("#"*70 + "\n")

def test_media_dias_por_plan(suscripciones: list[Suscripcion]):
    print("Test 'media_dias_por_plan'")
    media_dias_plan = media_dias_por_plan(suscripciones)
    print(f"Duración media (en días) de suscripciones finalizadas por tipo de plan: \n {media_dias_plan}")
    print("#"*70 + "\n")

def test_addon_mas_popular_por_año(suscripciones: list[Suscripcion]):
    print("Test 'addon_mas_popular_por_año'")
    addon_mas = addon_mas_popular_por_año(suscripciones)
    for ano, extras in addon_mas.items():
        print(f"En el año {ano} se contrataron estos servicios: {extras}")
    print("#"*70 + "\n")

def test_evolucion_años(suscripciones: list[Suscripcion]):
    print("Test 'evolucion_años'")
    evolucion = evolucion_años(suscripciones)
    print(f"Evolucion de suscripciones por año: \n {evolucion}")
    print("#"*70 + "\n")

def main():
    ruta = Path("Primer-Segundo-cuatrimestre/Sesion-3/data/suscripciones.csv")
    fichero = lee_suscripciones(ruta)

    test_lee_suscripciones(ruta)
    test_suscripciones_mas_rentables(fichero)
    test_plan_mas_perfiles(fichero)
    test_media_dias_por_plan(fichero)
    test_addon_mas_popular_por_año(fichero)
    test_evolucion_años(fichero)

if __name__=="__main__":
    main()