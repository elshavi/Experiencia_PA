
def cachipun():
    import random
    mcom = ""
    c = random.randint(1,3)
    #1.- piedra 2.- papel 3.- tijeras
    p = int(input("selecciona una de estas tres opciones: \n 1. -piedra \n 2. -papel \n 3. -tijeras \n"))
    
    if c == 1:
        pc = "piedra"
    elif c == 2:
        pc = "papel"
    elif c == 3:
        pc = "tijeras"

    if p == 1:
        persona = "piedra"
    elif p == 2:
        persona = "papel"
    elif p == 3:
        persona = "tijeras"
 

    if c == p:
        print("computadora: " + pc)
        print("tu: " + persona)
        print("empate")
    elif (c == 1 and p == 2) or (c == 2 and p == 3) or (c == 3 and p == 1):
        print("computadora: " + pc)
        print("tu: " + persona)
        print("tu ganas :D")
    else:
        print("computadora: " + pc) 
        print("tu: " + persona)
        print("perdiste :c")
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    pass
cachipun()