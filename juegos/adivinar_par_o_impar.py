import random

def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    prediction = input('Predice si el numero generado es par o impar')
    numero_generado = random.randint(1,10)
    if numero_generado % 2 == 0:
        numero_resultado = 'par'

    else:
        numero_resultado = 'impar'

    if prediction == numero_resultado:
        print(f'Felicidades, has acertado. El numero {numero_resultado} efectivamente es {numero_resultado}')

    else:
        print(f'Lo lamento, no has acertado tu prediccion. El numero {numero_generado} era {numero_resultado}')
    pass