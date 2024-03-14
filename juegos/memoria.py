import random

def memoria():

    secuencia = []
    for i in range(5):
        numero_generado = random.randint(1,20)
        secuencia.append(str(numero_generado))

    print(f'Memoriza la siguiente secuencia: {secuencia[0]}, {secuencia[1]}, {secuencia[2]}, {secuencia[3]}, {secuencia[4]}')

    respuesta = input("Escribe la secuencia, cuida poner un espacio luego de la coma")
    respuesta_list = respuesta.split(",")
    posicion = 0
    for numero_str in respuesta_list:
        respuesta_list[posicion] = numero_str.strip(" ")
    
    if secuencia == respuesta_list:
        print('Wow, tienes una memoria sorprendente, bienhecho.')
    else:
        print('Secuencia incorrecta, intentalo de nuevo')
        
    memoria()
    pass