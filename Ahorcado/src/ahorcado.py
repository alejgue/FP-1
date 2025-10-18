import random

def cargar_palabras(ruta):
    ''' 
    Recibe la ruta de un fichero de texto que contiene una palabra por línea y devuelve
    dichas palabras en una lista.    
    
    :param ruta: Ruta de un fichero de texto. El fichero debe contener una palabra por línea.
    :type ruta: str
    :return: Una lista con las palabras leías del fichero
    :rtype: list[str]
    '''
    
    with open(ruta, encoding='utf-8') as f: #abre un archivo de forma segura
        res = []
        for linea in f:
            res.append(linea.strip()) # strip() elimina los espacios en blanco y saltos de línea al principio y al final
        return res

def elegir_palabra(palabras: list[str]) -> str:
    '''
    Elige la palabra a adivinar:
    - Selecciona una palabra aleatoria de la lista 'palabras'
    - Devuelve la palabra seleccionada
    Ayuda: 
    - La función 'random.choice' del paquete 'random' recibe una lista de opciones y 
      devuelve una de ellas seleccionada aleatoriamente.

    :param palabras: Lista con las palabras a seleccionar
    :type palabras: list[str]
    :return: La palabra seleccionada
    :rtype: str
    '''
    #i = random.randint(0, len(palabras) - 1)
    #return palabras[i]
    return random.choice(palabras)

def enmascarar_palabra(palabra:str, letras_probadas:set[str]) -> str:
    '''
    Enmascarar la palabra:
    - Inicializar una lista vacía. 
    - Recorrer cada letra de la palabra, añadiendola a la cadena resultado 
      si forma parte de las letras_probadas, o añadiendo un '_' en caso contrario. 
    - Devuelve una cadena con la palabra enmascarada.
    
    :param palabra: Palabra que se quiere enmascarar
    :type palabra: str
    :param letras_probadas: Conjunto con las letras que ya se han probado
    :type letras_probadas: set[str]
    :return: La palabra original en la que las letras que no se han probado
       aparecen enmascaradas con un _.
    :rtype: str
    '''
    resultado = ""
    for letra in palabra:
        if letra in letras_probadas:
            resultado += letra
        else:
            resultado += '_'
    return resultado

def pedir_letra(letras_probadas:set[str]) -> str:
    '''
    Pedir la siguiente letra:
    - Pedirle al usuario que escriba la siguiente letra por teclado
    - Comprobar si la letra indicada es válida (tiene un solo caracter, es un caracter alfabético y no es una de las letras ya introducidas)
    - Mientras que la letra introducida no sea una letra válida, mostrar un mensaje de error y volver a pedir la letra
    - Considerar las letras en minúsculas aunque el usuario las escriba en mayúsculas
    - Devolver la letra
    Ayuda:
    - La función 'input' permite leer una cadena de texto desde la entrada estándar
    - El método 'lower' aplicado a una cadena devuelve una copia de la cadena en minúsculas
    - Defina dos funciones auxiliares:
        * letra_valida, que dado el conjunto de letras probadas y la letra introducida,
          devuelve True si la letra es válida, y False en caso contrario.
        * mensaje_error, que dados el conjunto de letras probads y una letra, devuelve un mensaje de error indicando,
          el motivo por el que la letra no es válida. Los mensajes de error deben ser:
               -  "Solo puedes introducir una letra. ", no tiene exactamente un caracter.
               -  "Debes introducir un carácter alfabético. ", si no introduce una letra.
               -  "Ya has introducido esa letra antes. ", si el problema es que ya introdujo esa letra.
    else:
        msg = "Ya has introducido esa letra antes. "
    :param letras_probadas: Conjunto con las letras que ya se han probado
    :type letras_probadas: set[str]
    :return: La letra que el usuario quiere probar
    :rtype: str
    '''
    letra = input("Introduce una letra: ").lower()
    while not letra_valida(letras_probadas, letra):
        print(mensaje_error(letras_probadas, letra))
        letra = input("Introduce una letra: ").lower()
    return letra

def letra_valida(letras_probadas:set[str], letra:str) -> bool:
    '''
    Dado el conjunto de letras probadas y la letra introducida,
    devuelve True si la letra es válida, y False en caso contrario.
    Una letra es válida si:
      - Tiene un solo caracter
      - Es un caracter alfabético
      - No es una de las letras ya introducidas
    '''
    if len(letra) != 1:
        return False
    if not letra.isalpha():
        return False
    if letra in letras_probadas:
        return False
    return True

def mensaje_error(letras_probadas:set[str], letra:str) -> str:
    '''
    Dados el conjunto de letras probads y una letra, devuelve un mensaje de error indicando,
    el motivo por el que la letra no es válida. Los mensajes de error deben ser:
         -  "Solo puedes introducir una letra. ", no tiene exactamente un caracter.
         -  "Debes introducir un carácter alfabético. ", si no introduce una letra.
         -  "Ya has introducido esa letra antes. ", si el problema es que ya introdujo esa letra.
    '''
    msg = ""
    if len(letra) != 1:
        msg = "Solo puedes introducir una letra. "
    elif not letra.isalpha():
        msg = "Debes introducir un carácter alfabético. "
    else:
        msg = "Ya has introducido esa letra antes. "
    return msg

def comprobar_letra(palabra_secreta:str, letra:str) -> bool:
    '''   
    Comprobar letra:
    - Comprobar si la letra está en la palabra secreta o no
    - Devolver True si estaba y False si no

    :param palabra_secreta: Palabra que se intenta adivinar
    :type palabra_secreta: str
    :param letra: letra que ha introducido el usuario
    :type letra: str
    :return: True si la letra está en la palabra
    :rtype: bool
    '''
    return letra in palabra_secreta

    #if letra in palabra_secreta:
    #    return True
    #else:
    #    return False    

    #for l in palabra_secreta:
    #    if l == letra:
    #        return True
    #return False

def mostrar_mensaje (acierto:bool):
    '''
    Mostrar mensaje:
     - Muestra por la consola el mensaje "¡Bien hecho! Esa letra está en la palabra.",
    si acierto tiene el valor True. 
    -  Muestra por la consola el mensaje "Lo siento, esa letra no está en la palabra."
    si acierto tiene el valor False.

    :param acierto: Es True si el usuario ha acertado la letra, y False en caso contrario
    :type acierto: bool
    '''
    if acierto:
        print("¡Bien hecho! Esa letra está en la palabra.")
    else:
        print("Lo siento, esa letra no está en la palabra.")

def comprobar_palabra_completa(palabra_secreta:str, letras_probadas:set[str]) -> bool:
    '''
    Comprobar si se ha completado la palabra:
    - Comprobar si todas las letras de la palabra secreta han sido propuestas por el usuario
    - Devolver True si es así o False si falta alguna letra por adivinar
    :param palabra_secreta: Palabra que se tiene que adivinar
    :type palabra_secreta: str
    :param letras_probadas: Conjunto con las letras que ya se han probado
    :type letras_probadas: set[str]
    :return: Devuelve True si se han adivinado todas las letras de la palabra, y False en caso contrario
    :rtype: bool
    '''
    return all(letra in letras_probadas for letra in palabra_secreta)  # True si todas las comparaciones dentro son True
    #for letra in palabra_secreta:                #in: verifica si esa letra ha sido adivinada
    #    if letra not in letras_probadas:
    #        return False
    #return True

def ejecutar_turno(palabra_secreta:str, letras_probadas:set[str]) -> bool:
    '''
    Ejecutar un turno de juego:
    - Mostrar la palabra enmascarada
    - Pedir la nueva letra
    - Añadir la letra al conjunto de letras probadas
    - Comprobar si la letra está en la palabra (acierto) o no (fallo)
    - Mostrar mensaje indicando acierto/fallo
    - Devolver True si la letra fue un acierto, False si fue un fallo
    Ayuda:
    - Recuerda las funciones que ya has implementado para mostrar la palabra, pedir la letra y comprobarla

    :param palabra_secreta: palabra que el usuario tiene que adivinar
    :type palabra_secreta: str
    :param letras_probadas: conjunto con las letras que el usuario ya ha probado
    :type letras_probadas: set [str]
    :return: True si el usuario ha adivinado la palabra, y False en caso contraro
    :rtype: bool
    '''
    print("Palabra: ", enmascarar_palabra(palabra_secreta, letras_probadas))
    letra = pedir_letra(letras_probadas)
    letras_probadas.add(letra)
    acierto = comprobar_letra(palabra_secreta, letra)
    mostrar_mensaje(acierto)
    return acierto

def jugar(max_intentos:int, palabras:list[str]):
    '''
      Completar una partida hasta que el jugador gane o pierda:
    - Mostrar mensaje de bienvenida
    - Elegir la palabra secreta a adivinar
    - Inicializar las variables del juego (letras probadas e intentos fallidos)
    - Ejecutar los turnos de juego necesarios hasta finalizar la partida, y en cada turno:
      > Averiguar si ha habido acierto o fallo
      > Actualizar el contador de fallos si es necesario
      > Comprobar si se ha superado el número de fallos máximo
      > Comprobar si se ha completado la palabra
      > Mostrar el mensaje de fin adecuado si procede o el número de intentos restantes

    :param max_intentos: Número máximo de intentos que el usuario tiene para adivinar la palabra
    :type max_intentos: int
    :param palabras: lista de palabras para adivinar
    :type palabras: list[str]
    '''
    print("¡Bienvenido al juego del Ahorcado!")
    palabra_secreta = elegir_palabra(palabras)
    print(palabra_secreta)
    letras_probadas = set()
    intentos_fallidos = 0

    while intentos_fallidos < max_intentos:
        acierto = ejecutar_turno(palabra_secreta, letras_probadas)
        if acierto:
            print("¡Felicidades! Has adivinado una letra.")
            if comprobar_palabra_completa(palabra_secreta, letras_probadas):
                print("¡Enhorabuena! ¡Has ganado! La palabra era:", palabra_secreta)
                return
        else:
            intentos_fallidos += 1
            print(f"Te quedan {max_intentos - intentos_fallidos} intentos.")

    print("¡Lo siento! Has perdido. La palabra era:", palabra_secreta)

if __name__ == "__main__":
    palabras = cargar_palabras("data/palabras_ahorcado.txt")
    jugar(6, palabras)