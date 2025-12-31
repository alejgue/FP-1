from piedra_papel_tijeras import *

def test_ordenador_decide_jugada():
    '''
    Test para la función ordenador_decide_jugada.
    '''
    print("Testeando ordenador_decide_jugada...")
    eleccion = ordenador_decide_jugada()
    print("El ordenador eligió:", eleccion)
    print()

def test_usuario_decide_jugada():
    '''
    Test para la función usuario_decide_jugada.
    '''
    print("Testeando usuario_decide_jugada...")
    eleccion = usuario_decide_jugada()
    print("El usuario eligió:", eleccion)
    print()

def test_determina_ganador(eleccion_jugador, eleccion_ordenador):
    '''
    Test para la función determina_ganador.
    '''
    print("Testeando determina_ganador...")        
    print(f"Jugador: {eleccion_jugador} vs. Ordenador: {eleccion_ordenador}")
    resultado = determina_ganador(eleccion_jugador, eleccion_ordenador)
    print("Resultado:", resultado)
    print()

# Función principal
if __name__ == "__main__":
    #test_ordenador_decide_jugada()
    #test_usuario_decide_jugada()
    try:
        test_ordenador_decide_jugada()
        test_usuario_decide_jugada()
    except Exception as e:
        print("Ocurrió un error al ejecutar test_ordenador_decide_jugada():", e)

     # Lista de combinaciones para probar determina_ganador
    combinaciones = [
        ("piedra", "tijeras"),
        ("piedra", "papel"),
        ("piedra", "piedra"),
        ("tijeras", "tijeras"),
        ("tijeras", "papel"),
        ("tijeras", "piedra"),
        ("papel", "tijeras"),
        ("papel", "papel"),
        ("papel", "piedra")
    ]

    for jugador, ordenador in combinaciones:
        test_determina_ganador(jugador, ordenador)
   