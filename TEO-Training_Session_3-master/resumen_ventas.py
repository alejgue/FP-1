"""Plantilla para el examen de entrada/salida: resumen de ventas."""

from __future__ import annotations

from datetime import date
from pathlib import Path


def resumen_ventas(path: Path) -> tuple[int, float]:
    """Lee el CSV y devuelve (total_registros_validos, promedio)."""
    raise NotImplementedError


def top_ventas(path: Path, n: int = 3) -> list[tuple[date, int]]:
    """Top-N de fechas con mayores ventas. Empata por fecha más reciente."""
    raise NotImplementedError


def fechas_faltantes(path: Path) -> list[date]:
    """Fechas ausentes entre la mínima y la máxima (ordenadas)."""
    raise NotImplementedError


def ventas_por_mes(path: Path) -> dict[str, tuple[int, float]]:
    """Mes (YYYY-MM) -> (total_registros, promedio_mes)."""
    raise NotImplementedError


def dias_por_encima(path: Path, umbral: int | None = None) -> list[date]:
    """Fechas con ventas superiores al umbral (o al promedio global si es None)."""
    raise NotImplementedError


def generar_reporte(registros: int, promedio: float) -> str:
    """Construye el contenido del reporte de texto."""
    raise NotImplementedError


def main() -> None:
    """CLI con argparse: lee rutas, genera resumen.txt y opcional resumen.json."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
