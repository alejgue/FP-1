---
main: "Entrada y salida"
sub: "Resumen de ventas"
---

# Fundamentos de Programación
## Práctica de patrones de examen: Resumen de ventas (entrada/salida)

**Objetivo**: practicar lectura y escritura de ficheros con `pathlib.Path`, manejo de errores, fechas, agregaciones simples y un CLI con `argparse` y salida JSON.

## Contexto

Dispones de un CSV con las ventas diarias de una tienda. El formato es `fecha,ventas` (fecha ISO `YYYY-MM-DD`, ventas enteras). Ejemplo:

```
fecha,ventas
2024-05-01,120
2024-05-02,150
```

## Observaciones

- Las rutas son relativas al directorio donde está `resumen_ventas.py` (`datos` y `reportes` viven allí).
- Puede haber líneas vacías o duplicadas; las vacías se ignoran.
- Usa UTF-8 y context managers (`with`) para abrir ficheros.
- Los mensajes al usuario deben ser claros tanto en éxito como en error (`FileNotFoundError`, `ValueError`).

## Estructura recomendada del proyecto

* **/entrada_salida_ejercicio/datos**: dataset `ventas_diarias.csv`.
* **/entrada_salida_ejercicio/reportes**: salidas `resumen.txt` y opcional `resumen.json`.
* **/entrada_salida_ejercicio/resumen_ventas.py**: funciones pedidas y el `main` con CLI.

## Ejercicios a implementar (en `resumen_ventas.py`)

1. **resumen_ventas(path: Path) -> tuple[int, float]** (1,5 puntos): lee el CSV, ignora filas vacías, convierte `ventas` a `int`, devuelve `(total_registros_validos, promedio)`. Si no hay datos válidos, lanza `ValueError` descriptivo. Propaga `FileNotFoundError` si la ruta no existe.
2. **top_ventas(path: Path, n: int = 3) -> list[tuple[date, int]]** (1 punto): devuelve las `n` fechas con mayores ventas, parseando `fecha` a `date`, ordenando por ventas descendentes y, en empate, por fecha más reciente.
3. **fechas_faltantes(path: Path) -> list[date]** (1 punto): detecta días ausentes entre la fecha mínima y máxima (sin contar duplicados ni filas vacías) y los devuelve ordenados.
4. **main con argparse y reporting** (2,5 puntos): acepta `--csv` (ruta de entrada) y `--salida` (directorio de reportes, por defecto `reportes`). Genera el directorio si no existe. Guarda `resumen.txt` con:

    ```
    Registros: <total>
    Promedio de ventas: <promedio con dos decimales>
    ```

    Además, si se pasa `--json`, crea `resumen.json` con: total, promedio, fecha de máximo, fecha de mínimo y la lista de fechas faltantes. Muestra mensajes claros si las rutas no existen o los datos son inválidos.
5. **ventas_por_mes(path: Path) -> dict[str, tuple[int, float]]** (1 punto): agrupa por mes (cadena `YYYY-MM`) y devuelve un diccionario mes → `(total_registros, promedio_del_mes)`.
6. **dias_por_encima(path: Path, umbral: int | None = None) -> list[date]** (1 punto): devuelve las fechas con ventas superiores al `umbral`; si es `None`, usa el promedio global como umbral. Ordena de menor a mayor fecha.

## Ejemplo de ejecución

```
$ python resumen_ventas.py --csv datos/ventas_diarias.csv
Reporte generado en: /ruta/completa/reportes/resumen.txt
```
