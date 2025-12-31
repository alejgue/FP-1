"""Procesa un CSV de ventas diarias y genera un resumen en un archivo de texto."""

from __future__ import annotations

import csv
from pathlib import Path
import os


def resumen_ventas(path: Path) -> tuple[int, float]:
    """Lee el CSV y devuelve el total de filas válidas y el promedio de ventas."""
    lineas = dict()  
    with path.open("r", encoding="utf-8") as fichero:
        lector=csv.reader(fichero) #devuelve cada fila como una lista de strings,
        next(lector)
        for fila in lector:
            if fila and any(cell.strip() != '' for cell in fila):
                 fecha, numero = fila
                 lineas[fecha] = int(numero) 
                 #try:
                    # Intentamos convertir el número a flotante para manejar decimales
                 #lineas[fecha] = float(numero)
                 #except ValueError:
                 #   continue  # Si no se puede convertir, saltamos esta filas
    if not path.exists():
        raise FileNotFoundError(path)
    if not lineas:
        raise ValueError("Los datos del registro no son validos")
    vlineas = len(lineas)
    promedio = sum(lineas.values()) / vlineas
    return vlineas, promedio

def generar_reporte(registros: int, promedio: float) -> str:
    """Construye el contenido del reporte."""
    return f"Registros: {registros}\nPromedio de ventas: {promedio:.2f}\n"


def main() -> None:
    ruta = Path('datos//ventas_diarias.csv')
    vlineas, promedio = resumen_ventas(ruta)
    if not Path('reportes'):
        os.mkdir("reportes")
    dfila = Path('C://.....//reportes//registros.txt') 

    with dfila.open("a") as f:
      f.write(generar_reporte(vlineas, promedio))
    print(f"Reporte generado en: {dfila}")

    

if __name__ == "__main__":
    main()


