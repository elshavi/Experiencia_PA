import random
def adivinar_numero():
    a = random.randint(1,10)
    print("he generado un numero al azar entre 1 y 10, adivinalo :o ")
    b = int(input("¿que numero crees que generé? "))
    if a == b:
        mau = "lo adivinaste :D"
    else:
        mau = "no lo adivinaste, el numero era" + str(a) + " , ahora moriras D:"
    print(mau)
    return
    
