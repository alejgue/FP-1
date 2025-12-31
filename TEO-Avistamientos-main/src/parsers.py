'''
Módulo que contiene funciones para conversión de tipos
'''
from datetime import datetime


def parse_datetime(cadena:str, formato:str = '%d/%m/%Y-%H:%M:%S')->datetime:
    '''Función que convierte una cadena con fecha y hora a un objeto datetime

    :param cadena: Cadena con la fecha y la hora
    :param formato: cadena con el formato de la fecha y la hora, el formato por defecto es '%d/%m/%Y-%H:%M:%S'
    :return: objeto fecha-hora
    '''
    return datetime.strptime(cadena, formato)

