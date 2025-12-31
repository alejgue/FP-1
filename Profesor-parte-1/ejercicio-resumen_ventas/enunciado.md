---
main: "Entrada y salida"
sub: "Resumen de ventas"
---

**Enunciado**

- En la carpeta `datos`, crea un archivo `ventas_diarias.csv` con cabecera `fecha,ventas` y al menos cinco registros reales.
- Implementa en `resumen_ventas.py` una función `resumen_ventas(path: Path) -> tuple[int, float]` que lea el CSV, ignore filas vacías e intente convertir la columna `ventas` a enteros.
- Calcula el número de registros válidos y el promedio de ventas. Si no hay datos válidos, levanta un `ValueError` con un mensaje descriptivo.
- Maneja `FileNotFoundError` al ejecutar el script principal mostrando un mensaje claro al usuario.
- Genera el directorio `reportes` si no existe y guarda un archivo `resumen.txt` con el formato:

```
Registros: <total>
Promedio de ventas: <promedio con dos decimales>
```

**Requisitos adicionales**

- Usa `pathlib.Path` para resolver rutas relativas a la carpeta del script.
- Asegúrate de cerrar los archivos correctamente empleando context managers (`with`).
- Proporciona mensajes de salida que indiquen dónde se guardó el reporte y, en caso de error, qué sucedió.

**Ejemplo de ejecución**

```
$ python resumen_ventas.py
Reporte generado en: /ruta/completa/reportes/resumen.txt
```
