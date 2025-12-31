# Fundamentos de Programación
## Práctica de patrones de examen: Gestión de envíos

**Objetivo**: que el alumno practique las lecturas múltiples de CSV (dos `NamedTuple`), filtros opcionales, contadores, medias, `defaultdict`, ordenaciones y recorridos consecutivos en el contexto de una empresa logística.

## Contexto

Tienes un histórico de **envíos** realizados para diferentes clientes y un fichero aparte con las **incidencias** asociadas a cada envío. Los datos están codificados en UTF-8 y utilizan fechas ISO (`YYYY-MM-DD`).

Ejemplo de líneas en `data/envios.csv`:

```
id_envio,cliente,fecha_salida,fecha_entrega,origen,destino,transporte,prioridad,segmento,peso_kg,coste
E001,TechNova,2024-01-02,2024-01-05,Madrid,Barcelona,Camion,ALTA,Electronica,450,780
E002,FrescoMarket,2024-01-04,2024-01-06,Valencia,Madrid,Refrigerado,ALTA,Alimentacion,320,650
```

Ejemplo de líneas en `data/incidencias.csv`:

```
id_envio,tipo,descripcion,dias_retraso,compensacion
E001,Demora,"Tráfico denso en AP-2",1,50
E004,Demora,"Control adicional en aduana",2,200
```

## NamedTuple obligatorias

```python
from typing import NamedTuple
from datetime import date

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
```

## Observaciones

- El conjunto de envíos **no** está ordenado por fecha.
- No todos los envíos tienen incidencias, pero cada incidencia referencia un `id_envio` válido.
- Las prioridades posibles son `ALTA`, `MEDIA` y `BAJA`.
- El número de días de tránsito es `(fecha_entrega - fecha_salida).days`.

## Estructura recomendada del proyecto

* **/envios/data**: datasets CSV del ejemplo.
* **/envios/src**: módulos Python con las funciones pedidas, sus soluciones y los tests.

## Ejercicios a implementar (en `src/envios.py`)

1. **lee_envios** y **lee_incidencias**: leen sus respectivos CSV y devuelven listas de `Envio` y `Incidencia`. (1,5 puntos)

    ```python
    def lee_envios(ruta: str) -> list[Envio]: ...
    def lee_incidencias(ruta: str) -> list[Incidencia]: ...
    ```

2. **coste_total**: suma el coste de los envíos, pudiendo filtrar por un cliente y/o un conjunto de prioridades. (1 punto)

    ```python
    def coste_total(envios: list[Envio], cliente: str | None = None, prioridades: set[str] | None = None) -> float: ...
    ```

3. **destinos_top_por_peso**: devuelve las `n` tuplas `(destino, peso_total)` con más peso enviado, ordenadas de mayor a menor. Se puede filtrar por tipo de transporte. (1 punto)

    ```python
    def destinos_top_por_peso(envios: list[Envio], transporte: str | None = None, n: int = 3) -> list[tuple[str, float]]: ...
    ```

4. **cliente_con_mas_incidencias**: usando envíos e incidencias, devuelve `(cliente, total_incidencias)` opcionalmente filtrando por tipos de incidencia. (1,5 puntos)

    ```python
    def cliente_con_mas_incidencias(envios: list[Envio], incidencias: list[Incidencia], tipos: set[str] | None = None) -> tuple[str, int]: ...
    ```

5. **retraso_medio_por_mes**: calcula un diccionario `mes -> retraso medio en días` (solo con envíos que tienen incidencias) con opción de filtrar por prioridad. (1,5 puntos)

    ```python
    def retraso_medio_por_mes(envios: list[Envio], incidencias: list[Incidencia], prioridad: str | None = None) -> dict[str, float]: ...
    ```

6. **segmento_mas_rentable**: devuelve el segmento con mayor facturación media (coste total / nº envíos) considerando solo segmentos con al menos `minimo_envios`. (1 punto)

    ```python
    def segmento_mas_rentable(envios: list[Envio], minimo_envios: int = 2) -> tuple[str, float]: ...
    ```

7. **dias_medios_entre_envios**: media de días entre salidas consecutivas ordenadas por fecha, pudiendo filtrar por cliente. (1 punto)

    ```python
    def dias_medios_entre_envios(envios: list[Envio], cliente: str | None = None) -> float: ...
    ```

Se anima a reutilizar helpers como `parse_fecha`, contadores y diccionarios auxiliares. Añade los tests necesarios en `src/envios_test.py` usando `unittest` o `pytest`.
