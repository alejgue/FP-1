from extranjeria import *
import csv

def test_lee_datos_extranjeria(ruta_fichero: Path) -> list[tuple]:

    print("Haciendo test de 'lee_datos_extranjeria'")
    lista = lee_datos_extranjeria(ruta_fichero)
    print(f"Leidos {len(lista)} registros.")
    print(f"Mostrando los 3 primeros: \n {lista[:3]}")
    print(f"Mostrando los 3 ultimos: \n {lista[-3:]}")
    print("#"*60 + "\n\n")

def test_numero_nacionalidades_distintas(registros: list[RegistroExtranjeria]) -> int:
    print("Haciendo test de 'numero_nacionalidades_distintas'")
    n_nacionalidades = numero_nacionalidades_distintas(registros)
    print(f"Hay {n_nacionalidades} distintas en los datos")
    print("#"*60 + "\n\n")

def test_secciones_distritos_con_extranjeros_nacionalidades(registros: list[RegistroExtranjeria],  paises: set[str]):
    print("Haciendo test de 'secciones_distritos_con_extranjeros_nacionalidades'")
    secciones = secciones_distritos_con_extranjeros_nacionalidades(registros, paises)
    paises_upper = set(pais.upper() for pais in paises)
    print(f"Hay {len(secciones)} secciones de distritos con residentes cuya procedencia es {paises_upper}.")
    print(f"Mostrando 3 secciones: \n {secciones[:3]} ")
    print("#"*60 + "\n\n")

def test_total_extranjeros_por_pais(registros: list[RegistroExtranjeria]):
    print("Haciendo test de 'total_extranjeros_por_pais'")
    n_residentes = total_extranjeros_por_pais(registros)
    muestra = list(n_residentes.items())[:3]
    print(f"Mostrando el numero de residentes para algunos paises de procedencia: \n {muestra}")
    print("#"*60 + "\n\n")


def test_top_n_extranjeria(registros: list[RegistroExtranjeria],  n=3):
    print("Haciendo test de 'top_n_extranjeria'")
    top = top_n_extranjeria(registros, n)
    print(f"Mostrando los {n} paises de los que proceden mas residentes: \n {top}")
    print("#"*60 + "\n\n")


def test_barrio_mas_multicultural(registros: list[RegistroExtranjeria]):
    print("Haciendo test de 'barrio_mas_multicultural'")
    barrio = barrio_mas_multicultural(registros)
    print(f"El barrio mas multicultural de sevilla es: {barrio}")
    print("#"*60 + "\n\n")


def test_barrio_con_mas_extranjeros(registros: list[RegistroExtranjeria], tipo=None):
    print("Haciendo test de 'barrio_con_mas_extranjeros'")
    barrio_2 = barrio_con_mas_extranjeros(registros, tipo)
    print(f"El barrio con mas {tipo} extranjeros de sevilla es: {barrio_2}")
    print("#"*60 + "\n\n")


def test_pais_mas_representado_por_distrito(registros: list[RegistroExtranjeria]):
    print("Haciendo test de 'pais_mas_representado_por_distrito'")
    paises_por_distrito = pais_mas_representado_por_distrito(registros)
    print("Los países con más residentes en cada distrito son los siguientes:")
    
    for distrito in sorted(paises_por_distrito.keys()):
        pais = paises_por_distrito[distrito]
        print(f"Distrito:{distrito} => {pais}")
        
    print("#" * 60 + "\n\n")


def main():
    ruta = Path("Profesor-parte-1/LAB-Extrajeria-main/data/extranjeriaSevilla.csv")
    fichero = lee_datos_extranjeria(ruta)

    test_lee_datos_extranjeria(ruta)
    test_numero_nacionalidades_distintas(fichero)
    test_secciones_distritos_con_extranjeros_nacionalidades(fichero, set(["Japon", "Gambia", "Noruega", "Alemania", "Paises bajos"]))
    test_total_extranjeros_por_pais(fichero)
    test_top_n_extranjeria(fichero, 3)
    test_barrio_mas_multicultural(fichero)
    test_barrio_con_mas_extranjeros(fichero, None)
    test_pais_mas_representado_por_distrito(fichero)

if __name__ == "__main__":
    main()
    