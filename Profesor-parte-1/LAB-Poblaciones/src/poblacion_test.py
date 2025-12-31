from poblacion import *

def lee_poblaciones_test(ruta_fichero):
    print("Testeando lee_poblaciones()... ")
    poblaciones = lee_poblaciones(ruta_fichero)
    print(f"Leídos {len(poblaciones)} registros.")
    print(f"Los tres primeros son: {poblaciones[:3]}")
    print(f"Los tres últimos son: {poblaciones[-3:]}\n")

def calcula_paises_test(poblaciones):
    print("Testeando calcula_paises()... ")
    paises = calcula_paises(poblaciones)
    print(f"Se han encontrado {len(paises)} países.")
    print(f"Los diez primeros son: {paises[:10]}\n")

def filtra_por_pais_test(poblaciones, nombre_o_codigo):
    print(f"Testeando filtra_por_pais() para '{nombre_o_codigo}'... ")
    datos_pais = filtra_por_pais(poblaciones, nombre_o_codigo)
    print(f"Año y censo (primeros 5): {datos_pais[:5]}\n")

def filtra_por_paises_y_anyo_test(poblaciones, anyo, paises):
    print(f"Testeando filtra_por_paises_y_anyo() para el año {anyo}... ")
    paises_filtrados = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    print(f"Resultado: {paises_filtrados}\n")

def muestra_evolucion_poblacion_test(poblaciones, nombre_o_codigo):
    print(f"Generando gráfica de evolución para '{nombre_o_codigo}'... ")
    muestra_evolucion_poblacion(poblaciones, nombre_o_codigo)

def muestra_comparativa_paises_anyo_test(poblaciones, anyo, paises):
    print(f"Ejecutando comparativa para el año {anyo} de los países: {paises}...")
    muestra_comparativa_paises_anyo(poblaciones, anyo, paises)

if __name__ == "__main__":
    # 1. Cargar los datos iniciales
    ruta = 'data/population.csv'
    datos = lee_poblaciones(ruta)
    
    # 2. Ejecutar las pruebas
    lee_poblaciones_test(ruta)
    calcula_paises_test(datos)
    filtra_por_pais_test(datos, 'Spain')
    filtra_por_paises_y_anyo_test(datos, 2016, ['Spain', 'Germany', 'France'])
    muestra_evolucion_poblacion_test(datos, 'Spain')
    muestra_comparativa_paises_anyo_test(datos, 2016, ['Spain', 'Germany', 'France', 'Italy'])