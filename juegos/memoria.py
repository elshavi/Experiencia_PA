import random

def memoria():

    n1 = str(random.randint(1,20))
    n2 = str(random.randint(1,20))
    n3 = str(random.randint(1,20))
    n4 = str(random.randint(1,20))
    n5 = str(random.randint(1,20))

    secuencia = n1 + "-" + n2 + "-" + n3 + "-" + n4 + "-" + n5
    print(f'Memoriza la siguiente secuencia {secuencia}')

    respuesta = input('Escribe la secuencia, separando los numeros con un guion')
    if secuencia == respuesta:
        print('WOW, tu memoria es increible.')
    else:
        print('Secuencia incorrecta, intentalo de nuevo.')
    
    pass