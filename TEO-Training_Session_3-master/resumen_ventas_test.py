from pathlib import Path
from datetime import date
from resumen_ventas import (
    resumen_ventas, 
    top_ventas, 
    fechas_faltantes, 
    ventas_por_mes, 
    dias_por_encima
)

def test_procesamiento():
    csv_path = Path("ventas_diarias.csv")
    
    print("--- Test: resumen_ventas ---")
    regs, prom = resumen_ventas(csv_path)
    print(f"Registros: {regs} (Esperado: 5)")
    print(f"Promedio: {prom} (Esperado: 147.0)")
    assert regs == 5
    assert prom == 147.0

    print("\n--- Test: top_ventas ---")
    top = top_ventas(csv_path, n=2)
    print(f"Top 2: {top}")
    # El máximo es 200 el 2024-05-04, luego 175 el 2024-05-05
    assert top[0] == (date(2024, 5, 4), 200)

    print("\n--- Test: fechas_faltantes ---")
    faltan = fechas_faltantes(csv_path)
    print(f"Faltantes: {faltan} (Esperado: [])")
    # En tu CSV de ejemplo (01 al 05) no falta ningún día
    assert len(faltan) == 0

    print("\n--- Test: ventas_por_mes ---")
    meses = ventas_por_mes(csv_path)
    print(f"Agrupado: {meses}")
    assert "2024-05" in meses
    assert meses["2024-05"][0] == 5

    print("\n--- Test: dias_por_encima ---")
    encima = dias_por_encima(csv_path, umbral=150)
    print(f"Días > 150: {encima}")
    # 150 no es mayor que 150, así que solo deben salir 200 y 175
    assert len(encima) == 2

    print("\n✅ ¡Todas las pruebas locales pasaron con éxito!")

if __name__ == "__main__":
    test_procesamiento()

    # Generar TXT estándar: python resumen_ventas.py --csv ventas_diarias.csv
    # Generar TXT y JSON en una carpeta específica: python resumen_ventas.py --csv ventas_diarias.csv --salida mis_reportes --json