from __future__ import annotations

from datetime import date, datetime
from typing import NamedTuple


class Envio(NamedTuple):
    id_envio: str
    cliente: str
    fecha_salida: date
    fecha_entrega: date
    origen: str
    destino: str
    transporte: str
    prioridad: str
    segmento: str
    peso_kg: float
    coste: float


class Incidencia(NamedTuple):
    id_envio: str
    tipo: str
    descripcion: str
    dias_retraso: int
    compensacion: float


MESES = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}


def parse_fecha(cadena: str) -> date:
    """Convierte fecha ISO (YYYY-MM-DD) a date."""
    return datetime.strptime(cadena, "%Y-%m-%d").date()


def lee_envios(ruta: str) -> list[Envio]:
    """Lee el CSV de envíos."""
    raise NotImplementedError


def lee_incidencias(ruta: str) -> list[Incidencia]:
    """Lee el CSV de incidencias."""
    raise NotImplementedError


def coste_total(
    envios: list[Envio],
    cliente: str | None = None,
    prioridades: set[str] | None = None,
) -> float:
    """Suma el coste total aplicando filtros opcionales."""
    raise NotImplementedError


def destinos_top_por_peso(
    envios: list[Envio],
    transporte: str | None = None,
    n: int = 3,
) -> list[tuple[str, float]]:
    """Top-N de destinos según el peso enviado."""
    raise NotImplementedError


def cliente_con_mas_incidencias(
    envios: list[Envio],
    incidencias: list[Incidencia],
    tipos: set[str] | None = None,
) -> tuple[str, int]:
    """Cliente con mayor número de incidencias (opcionalmente filtradas)."""
    raise NotImplementedError


def retraso_medio_por_mes(
    envios: list[Envio],
    incidencias: list[Incidencia],
    prioridad: str | None = None,
) -> dict[str, float]:
    """Diccionario mes -> retraso medio en días para esa prioridad."""
    raise NotImplementedError


def segmento_mas_rentable(
    envios: list[Envio],
    minimo_envios: int = 2,
) -> tuple[str, float]:
    """Segmento con mayor facturación media, restringiendo por nº mínimo de envíos."""
    raise NotImplementedError


def dias_medios_entre_envios(
    envios: list[Envio],
    cliente: str | None = None,
) -> float:
    """Media de días entre salidas consecutivas."""
    raise NotImplementedError


if __name__ == "__main__":
    import pathlib

    base = pathlib.Path(__file__).resolve().parent.parent / "data"
    print(base)
