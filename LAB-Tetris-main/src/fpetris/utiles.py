from typing import List

def inicializa_tablero(ancho_tablero: int, alto_tablero: int) -> List[List[int]]:
    """
    Inicializa el tablero del juego con un tamaño especificado.

    Parámetros:
    - ancho_tablero (int): Ancho del tablero (número de columnas).
    - alto_tablero (int): Altura del tablero (número de filas).

    Devuelve:
    - List[List[int]]: Una matriz (lista de listas) representando el tablero,
      inicializada con Nones, donde cada None representa una celda vacía.

    Ejemplo:
    >>> inicializa_tablero(3, 2)
    [[None, None, None], [None, None, None]]
    """
    filas = []
    for i in range(alto_tablero):
        fila = []
        for j in range(ancho_tablero):
            fila.append(None)
        filas.append(fila)    
    return filas

def coloca_pieza(tablero: List[List[str]], pieza: List[List[bool]], x: int, y: int, color: str) -> None:
    """
    Coloca una pieza en el tablero en una posición especificada. Se supone que la pieza 
    cabe correctamente en el tablero (no hay que comprobarlo).

    Parámetros:
    - tablero (List[List[str]]): El tablero del juego.
    - pieza (List[List[bool]]): La pieza a colocar, representada como una lista de listas de booleanos.
    - x (int): Posición en el eje X (columna) donde se coloca la esquina superior izquierda de la pieza.
    - y (int): Posición en el eje Y (fila) donde se coloca la esquina superior izquierda de la pieza.
    - color (str): Color asignado a la pieza.

    No devuelve nada (None).

    Ejemplo:
    >>> tablero = [[None, None, None], [None, None, None], [None, None, None]]
    >>> pieza = [[True, True], [False, True]]
    >>> coloca_pieza(tablero, pieza, 1, 1, 'red')
    >>> tablero
    [[None, None, None], [None, 'red', 'red'], [None, None, 'red']]
    """
    for fila_pieza in range(len(pieza)):
        for col_pieza in range(len(pieza[0])):
            if pieza[fila_pieza][col_pieza]:
                tablero[y + fila_pieza][x + col_pieza] = color  
    

def busca_filas_completas(tablero: List[List[str]]) -> List[int]:
    """
    Identifica las filas completas (sin celdas vacías) en el tablero.

    Parámetros:
    - tablero (List[List[str]]): El tablero del juego.

    Devuelve:
    - List[int]: Lista de índices de las filas completas.

    Ejemplo:
    >>> tablero = [['red', 'red', 'red'], [None, 'red', None], ['blue', 'blue', 'blue']]
    >>> busca_filas_completas(tablero)
    [0, 2]
    """
    
    filas_completas = []
    for i in range(len(tablero)):
        if not None in tablero[i]:
            filas_completas.append(i)
    return filas_completas

def posicion_valida(tablero: List[List[str]], pieza: List[List[bool]], pieza_x: int, pieza_y: int) -> bool:
    """
    Verifica si la posición de una pieza es válida en el tablero (no colisiona con otras piezas ni se sale 
    de los bordes del tablero).

    Parámetros:
    - tablero (List[List[str]]): El tablero del juego.
    - pieza (List[List[bool]]): La pieza a verificar.
    - pieza_x (int): Posición en el eje X (columna) de la esquina superior izquierda de la pieza.
    - pieza_y (int): Posición en el eje Y (fila) de la esquina superior izquierda de la pieza.

    Devuelve:
    - bool: True si la posición es válida, False en caso contrario.

    Ejemplos:
    >>> tablero = [[None, None, None], [None, 'red', None], [None, None, None]]
    >>> pieza = [[True, True], [True, False]]
    >>> posicion_valida(tablero, pieza, 0, 1)  # No colisiona, ni se sale del tablero
    True
    >>> posicion_valida(tablero, pieza, 1, 1)  # Colisiona con 'red'
    False
    >>> posicion_valida(tablero, pieza, -1, 1)  # Se sale del tablero por la izquierda
    False
    >>> posicion_valida(tablero, pieza, 2, 1)  # Se sale del tablero por la derecha
    False    
    """
    for fila_pieza in range(len(pieza)):
        for col_pieza in range(len(pieza[0])):
            if pieza[fila_pieza][col_pieza]:
                tablero_x = pieza_x + col_pieza
                tablero_y = pieza_y + fila_pieza
                
                # Comprobar si la posición está fuera de los límites del tablero
                if (tablero_x < 0 or tablero_x >= len(tablero[0]) or
                    tablero_y < 0 or tablero_y >= len(tablero)):
                    return False
                
                # Comprobar si la posición colisiona con una pieza existente
                if tablero[tablero_y][tablero_x] is not None:
                    return False
    return True  

def rota_pieza(pieza: List[List[bool]]) -> List[List[bool]]:
    """
    Rota una pieza 90 grados en sentido horario. La rotación se realiza en dos pasos:
    1. Invertir el orden de las filas de la pieza.
    2. Transponer la matriz resultante.

    Parámetros:
    - pieza (List[List[bool]]): La pieza a rotar.

    Devuelve:
    - List[List[bool]]: La pieza rotada.

    Ejemplo:
    >>> pieza = [[True, False, True], [False, True, False]]
    >>> rota_pieza(pieza)
    [[False, True], [True, False], [False, True]]
    """
    
    pieza_invertida = pieza[::-1]
    pieza_rotada = []
    for col in range(len(pieza_invertida[0])):
        nueva_fila = []
        for fila in range(len(pieza_invertida)):
            nueva_fila.append(pieza_invertida[fila][col])
        pieza_rotada.append(nueva_fila)
    return pieza_rotada