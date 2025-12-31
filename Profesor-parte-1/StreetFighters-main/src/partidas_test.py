from partidas import *

def test_lee_fichero(ruta):
    print(f"--- Testeando lee_fichero con '{ruta}' ---")
    partidas = lee_fichero(ruta)
    print(f"Total de partidas leídas: {len(partidas)}")
    if partidas:
        print(f"Primera partida: {partidas[0]}")
    print("-" * 50)
    return partidas

def test_victora_mas_rapida(partidas:List[Partida]):
    print("testeando victoria mas rapida")
    victoria = victora_mas_rapida(partidas)
    print(f"La victorias mas rapida es de {victoria}")
    print("-" * 50)

def test_top_ratio_medio_personajes(partidas:List[Partida], n:int):
    print("testeando top_ratio_medio_personajes")
    top_ratio = top_ratio_medio_personajes(partidas, n)
    print(f"El top ratio medio de personajes es de {top_ratio}")
    print("-" * 50)

def test_enemigos_mas_debiles(partidas, personaje):
    print(f"--- Testeando enemigos_mas_debiles para '{personaje}' ---")
    resultado = enemigos_mas_debiles(partidas, personaje)
    print(f"Resultado (Máx derrotas, Enemigos): {resultado}")
    print("-" * 50)

def test_movimientos_comunes(partidas, p1, p2):
    print(f"--- Testeando movimientos_comunes entre '{p1}' y '{p2}' ---")
    comunes = movimientos_comunes(partidas, p1, p2)
    print(f"Movimientos en común: {comunes}")
    print("-" * 50)

def test_dia_mas_combo_finish(partidas):
    print("--- Testeando dia_mas_combo_finish ---")
    dias = dia_mas_combo_finish(partidas)
    print(f"Día(s) con más combo finish: {dias}")
    print("-" * 50)

if __name__ == "__main__":
    fichero = "Profesor-parte-1/StreetFighters-main//data/games.csv"
    
    # 2. Ejecutamos los tests de forma secuencial
    try:
        # Cargamos los datos
        lista_partidas = test_lee_fichero(fichero)
        
        if lista_partidas:
            test_victora_mas_rapida(lista_partidas)
            test_top_ratio_medio_personajes(lista_partidas, 3)
            test_enemigos_mas_debiles(lista_partidas, "Ryu")
            test_movimientos_comunes(lista_partidas, "Ryu", "Ken")
            test_dia_mas_combo_finish(lista_partidas)
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{fichero}'. Asegúrate de que esté en la misma carpeta.")
    except Exception as e:
        print(f"Ocurrió un error durante los tests: {e}")