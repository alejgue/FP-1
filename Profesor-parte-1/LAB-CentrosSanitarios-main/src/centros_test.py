from coordenadas import Coordenadas, calcular_distancia, calcular_media_coordenadas
from centros import leer_centros, obtener_centros_con_uci_cercanos_a, generar_mapa

def test_coordenadas():
    print("=== 1. TEST DE COORDENADAS ===")
    p1 = Coordenadas(36.13, -5.84)
    p2 = Coordenadas(36.18, -5.92)
    
    dist = calcular_distancia(p1, p2)
    print(f"Distancia entre p1 y p2: {dist:.4f}")
    
    media = calcular_media_coordenadas([p1, p2])
    print(f"Media (Centroide) de p1 y p2: {media}")
    print("-" * 30)

def test_centros():
    print("=== 2. TEST DE CARGA Y FILTRADO ===")
    # Cargamos los datos del CSV
    ruta_csv = 'centrosSanitarios.csv'
    datos = leer_centros(ruta_csv)
    print(f"Total de centros cargados: {len(datos)}")
    
    if datos:
        # Mostramos el primero para verificar la carga
        print(f"Primer centro: {datos[0].nombre} en {datos[0].localidad}")
        
        # Probamos buscar centros con UCI cerca de un punto (ej: Barbate)
        mi_ubicacion = Coordenadas(36.18, -5.92)
        umbral = 0.5 # Radio de búsqueda
        
        cercanos = obtener_centros_con_uci_cercanos_a(datos, mi_ubicacion, umbral)
        print(f"Centros con UCI en un radio de {umbral} de mi ubicación: {len(cercanos)}")
        for nombre, local, coord in cercanos:
            print(f" - {nombre} ({local})")
            
        # Generamos el mapa si hay resultados
        if cercanos:
            print("\nGenerando mapa 'centros_cercanos.html'...")
            generar_mapa(cercanos, "centros_cercanos.html")
            print("¡Mapa creado con éxito!")
    print("-" * 30)

if __name__ == "__main__":
    try:
        test_coordenadas()
        test_centros()
        print("\n>>> TODAS LAS PRUEBAS COMPLETADAS CON ÉXITO <<<")
    except Exception as e:
        print(f"\n❌ Error durante los tests: {e}")