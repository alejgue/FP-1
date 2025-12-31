from collections import namedtuple

import csv
import matplotlib.pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero: str) -> list[RegistroPoblacion]:
    with open(ruta_fichero, encoding='utf-8') as f:
        reader = csv.reader(f)
        return [RegistroPoblacion(*fila) for fila in reader]


def calcula_paises(poblaciones: list[RegistroPoblacion]) -> list[str]:
   no_duplicados = set()
   for linea in poblaciones:
       #if linea.codigo is None and linea.año is None and linea.censo is None:
       #if not linea.codigo or not linea.año or not linea.censo:    
       #    continue   
       # else
       no_duplicados.add(linea.pais)
   no_duplicados_ordenados = sorted(no_duplicados)
   return no_duplicados_ordenados


def filtra_por_pais(poblaciones: list[RegistroPoblacion], nombre_o_codigo: str) -> list[tuple[int,int]]:
    conjunto_de_resultados = list()
    for linea in poblaciones:
        if linea.pais == nombre_o_codigo or linea.codigo == nombre_o_codigo:
            conjunto_de_resultados.append((int(linea.año), int(linea.censo)))
    return conjunto_de_resultados


def filtra_por_paises_y_anyo(poblaciones: list[RegistroPoblacion], anyo: int, paises: list[str]) -> list[tuple[str,int]]:
    conjunto_de_resultados = list()
    for linea in poblaciones:
        if(linea.pais in paises and int(linea.año)==anyo):
            conjunto_de_resultados.append((str(linea.pais), int(linea.censo)))
    return conjunto_de_resultados


def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    filtrado=filtra_por_pais(poblaciones, nombre_o_codigo)
    paises=[]
    poblacion=[]
    for linea in filtrado:
        paises.append(linea[0])
        poblacion.append(linea[1])
    genera_grafica_evolucion_poblacion("Evolución de la población de "+nombre_o_codigo, paises, poblacion)

def genera_grafica_evolucion_poblacion(titulo:str, lista_años:list[int], lista_habitantes:list[int]):
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()



def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    """
    Muestra una gráfica de barras comparando la población de varios países en un año concreto.
    """
    # 1. Obtenemos los datos filtrados usando la función existente
    datos_filtrados = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    
    # 2. Preparamos las listas para la gráfica
    nombres_paises = [nombre for nombre, censo in datos_filtrados]
    censos = [censo for nombre, censo in datos_filtrados]
    
    # 3. Definimos el título y generamos la gráfica
    titulo = f"Comparativa de población en el año {anyo}"
    genera_grafica_barras(titulo, nombres_paises, censos)

def genera_grafica_barras(titulo, etiquetas, valores):
    """
    Genera y muestra una gráfica de barras.
    """
    plt.title(titulo)
    plt.bar(etiquetas, valores) # Crea el diagrama de barras
    plt.ylabel("Número de habitantes")
    plt.show()



if __name__ == '__main__':
    poblaciones=lee_poblaciones('data/population.csv')
    paises=calcula_paises(poblaciones)
    
    spain=filtra_por_pais(poblaciones, 'Spain')     # cuidado con la ruta del terminal
    alemania=filtra_por_pais(poblaciones, 'DEU')       # https://docs.python.org/es/3.9/library/csv.html   puede entrar examen

    paises_anyo=filtra_por_paises_y_anyo(poblaciones, 2016, ['Spain', 'Germany'])
    print(paises_anyo)

    muestra_evolucion_poblacion(poblaciones, 'DEU')