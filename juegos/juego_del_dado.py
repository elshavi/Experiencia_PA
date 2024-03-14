import random

def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    suma_jugador = 0
    suma_computador = 0
    
    while suma_jugador < 30 and suma_computador < 30:
        input('Presione ENTER para lanzar un dado')
        dado_jugador = random.randint(1,6)
        suma_jugador += dado_jugador
        print(f'Has lanzado un dado, y has obtenido un {dado_jugador}. Llevas {suma_jugador} puntos.')

        dado_computador = random.randint(1,6)
        suma_computador += dado_computador
        print(f'El computador ha lanzado un dado, y ha obtenido un {dado_computador}. El computador lleva {suma_computador} puntos.')

    if suma_computador >= 30:
        print(f'Has perdido, computador gano con {suma_computador} puntos.')
    
    else:
        print(f'Has ganado al computador, sumando {suma_jugador} puntos.')
    pass