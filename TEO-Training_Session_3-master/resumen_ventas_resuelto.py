"""Módulo de resumen de ventas con entrada/salida y procesamiento de fechas."""

from __future__ import annotations
import csv
import json
import argparse
from datetime import date, datetime, timedelta
from pathlib import Path
from collections import defaultdict

def resumen_ventas(path: Path) -> tuple[int, float]:
    """Lee el CSV y devuelve (total_registros_validos, promedio)."""
    if not path.exists():
        raise FileNotFoundError(f"El archivo {path} no existe")
    
    with path.open('r', encoding="utf-8") as fichero:
        lector = csv.reader(fichero)
        next(lector)  # Cabecera

        total_registros = 0
        suma_ventas = 0.0

        for linea in lector:
            if not linea or not any(linea): # Ignorar líneas vacías
                continue
            total_registros += 1 
            suma_ventas += float(linea[1])

        if total_registros == 0:
            raise ValueError("No hay registros válidos en el archivo")

        promedio = suma_ventas / total_registros

    return total_registros, promedio

def _leer_datos_csv(path: Path) -> list[tuple[date, int]]:
    """Función auxiliar para leer y parsear los datos del CSV."""
    datos = []
    with path.open('r', encoding="utf-8") as fichero:
        lector = csv.reader(fichero)
        next(lector)
        for linea in lector:
            if linea and any(linea):
                fecha = date.fromisoformat(linea[0])
                ventas = int(linea[1])
                datos.append((fecha, ventas))
    return datos

def top_ventas(path: Path, n: int = 3) -> list[tuple[date, int]]:
    """Top-N de fechas con mayores ventas. Empata por fecha más reciente."""
    datos = _leer_datos_csv(path)
    # Ordenar por ventas (desc) y luego por fecha (desc)
    datos_ordenados = sorted(datos, key=lambda x: (x[1], x[0]), reverse=True)
    return datos_ordenados[:n]

def fechas_faltantes(path: Path) -> list[date]:
    """Detecta días ausentes entre la fecha mínima y máxima."""
    datos = _leer_datos_csv(path)
    if not datos:
        return []
    
    fechas_existentes = {d[0] for d in datos}
    fecha_min = min(fechas_existentes)
    fecha_max = max(fechas_existentes)
    
    faltantes = []
    actual = fecha_min
    while actual <= fecha_max:
        if actual not in fechas_existentes:
            faltantes.append(actual)
        actual += timedelta(days=1)
    
    return sorted(faltantes)

def ventas_por_mes(path: Path) -> dict[str, tuple[int, float]]:
    """Mes (YYYY-MM) -> (total_registros, promedio_mes)."""
    datos = _leer_datos_csv(path)
    agrupado = defaultdict(list)
    
    for fecha, ventas in datos:
        mes = fecha.strftime("%Y-%m")
        agrupado[mes].append(ventas)
    
    resultado = {}
    for mes, ventas_lista in agrupado.items():
        total = len(ventas_lista)
        promedio = sum(ventas_lista) / total
        resultado[mes] = (total, promedio)
    
    return resultado

def dias_por_encima(path: Path, umbral: int | None = None) -> list[date]:
    """Fechas con ventas superiores al umbral o al promedio global."""
    if umbral is None:
        _, umbral = resumen_ventas(path)
    
    datos = _leer_datos_csv(path)
    return [fecha for fecha, ventas in datos if ventas > umbral]

def generar_reporte(registros: int, promedio: float) -> str:
    """Construye el contenido del reporte de texto."""
    return f"Registros: {registros}\nPromedio de ventas: {promedio:.2f}\n"

def main() -> None:
    parser = argparse.ArgumentParser(description="Procesador de ventas diarias.")
    parser.add_argument("--csv", type=str, default="datos/ventas_diarias.csv", help="Ruta al CSV")
    parser.add_argument("--salida", type=str, default="reportes", help="Directorio de salida")
    parser.add_argument("--json", action="store_true", help="Generar reporte JSON adicional")
    
    args = parser.parse_args()
    csv_path = Path(args.csv)
    salida_dir = Path(args.salida)
    
    try:
        salida_dir.mkdir(parents=True, exist_ok=True)
        
        # 1. Obtener datos básicos
        regs, prom = resumen_ventas(csv_path)
        
        # 2. Generar TXT
        txt_path = salida_dir / "resumen.txt"
        txt_path.write_text(generar_reporte(regs, prom), encoding="utf-8")
        
        # 3. Generar JSON si se solicita
        if args.json:
            datos = _leer_datos_csv(csv_path)
            fechas = [d[0] for d in datos]
            reporte_json = {
                "total": regs,
                "promedio": round(prom, 2),
                "fecha_max": str(max(fechas)),
                "fecha_min": str(min(fechas)),
                "fechas_faltantes": [str(f) for f in fechas_faltantes(csv_path)]
            }
            json_path = salida_dir / "resumen.json"
            with json_path.open('w', encoding="utf-8") as f:
                json.dump(reporte_json, f, indent=4)
        
        print(f"Proceso finalizado. Reportes generados en: {salida_dir}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error en los datos: {e}")

if __name__ == "__main__":
    main()