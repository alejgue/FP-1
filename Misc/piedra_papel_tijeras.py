import random

opciones = ["piedra","papel","tijeras"]

def ordenador_decide_jugada():
    '''
    Elige aleatoriamente entre piedra. papel o tijera.
    '''
    i = random.randint(0,2)
    return opciones[i]

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while (not (eleccion_usuario in opciones)):
        eleccion_usuario = input("Opcion invalida; Elige piedra, papel o tijeras:")    
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if (jugada_usuario not in opciones) or (jugada_ordenador not in opciones):
       return "No vale" 
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijera" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"
    
def jugar():
    print("Bienvenido a PP")
    pc=ordenador_decide_jugada()
    jugador=usuario_decide_jugada()
    resultado=determina_ganador(jugada_usuario=jugador, jugada_ordenador=pc)
    print("El pc ha elegido:", pc)
    print(resultado)

def jugar_torneo(rondas:int):
    print("Bienvenido al tornaco vamos a jugar " + str(rondas) + " veces")
    jugadas=0
    puntos_pc=0
    puntos_jugador=0

    while (jugadas!=rondas):
        pc=ordenador_decide_jugada()
        jugador=usuario_decide_jugada()
        resultado=determina_ganador(jugada_usuario=jugador, jugada_ordenador=pc)
        if resultado == "Ganaste":
            puntos_jugador+=1
            jugadas+=1
        elif resultado == "Perdiste":
            puntos_pc+=1
            jugadas+=1

        print("En esta ronda " + resultado)
    
    print("Ganaste " + str(puntos_jugador) + " veces y perdiste " + str(puntos_pc) + " veces")
    if puntos_jugador > puntos_pc:
        print("Ganaste la partida")
    else:
        print("perdiste la partida")
if __name__ == "__main__":
    opcion = input("¿Quieres jugar (1) una partida o (2) un torneo?: ")
    if opcion == "1":
        jugar()
    elif opcion == "2":
        rondas = int(input("¿Cuántas rondas quieres jugar?: "))
        jugar_torneo(rondas)