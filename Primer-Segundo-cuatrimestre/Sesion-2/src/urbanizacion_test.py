from urbanizacion import *

def test_lee_viviendas(ruta: str):
    print("testeando 'lee_viviendas'")
    fichero = lee_viviendas(ruta)
    print(f"El numero de registros es {len(fichero)}\n")
    print(f"Las dos primeras: {fichero[:2]}\n")
    print(f"Las dos ultimas: {fichero[-2:]}\n")
    print("#"*70)

def test_total_mejoras_por_calle(viviendas: list[Vivienda], par_impar: str):
    print("testeando 'total_mejoras_por_calle'")
    mejoras = total_mejoras_por_calle(viviendas, par_impar)
    print(f"Numero de mejoras en viviendas {par_impar}\n")
    print(f"{mejoras}")
    print("#"*70)

def test_vivienda_con_mejora_mas_rapida(viviendas: list[Vivienda]):
    print("testeando 'vivienda_con_mejora_mas_rapida'")
    mas_rapida = vivienda_con_mejora_mas_rapida(viviendas)
    print(f"La vivienda que hizo una mejora en menos tiempo es {mas_rapida}")
    print("#"*70)

def test_calle_mayor_diferencia_precios(viviendas: list[Vivienda]):
    print("testeando 'calle_mayor_diferencia_precios'")
    mas_diferencia = calle_mayor_diferencia_precios(viviendas)
    print(f"La calle es: {mas_diferencia}")
    print("#"*70)

def test_valor_metro_cuadrado_por_calle_y_año(viviendas: list[Vivienda]):
    print("testeando 'valor_metro_cuadrado_por_calle_y_año'")
    metro_cuadrado = valor_metro_cuadrado_por_calle_y_año(viviendas)
    print(metro_cuadrado)
    print("#"*70)

def main():

    ruta = "Primer-Segundo-cuatrimestre/Sesion-2/data/urbanizacion.csv" # No poner \, da error

    fichero = lee_viviendas(ruta)

    test_lee_viviendas(ruta)
    test_total_mejoras_por_calle(fichero, "impar")
    test_vivienda_con_mejora_mas_rapida(fichero)
    test_calle_mayor_diferencia_precios(fichero)
    test_valor_metro_cuadrado_por_calle_y_año(fichero)

if __name__== "__main__":
    main()
