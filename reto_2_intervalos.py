# Generar un número aleatorio entre 1 y 120. Decir si se encuentra en el intervalo entre 10 y 50, 
# o bien si es mayor de 50 hasta 100, o bien si es mayor de 100, o bien si es menor de 10.

from random import randint

def numero():
    num = randint(1, 120)

    if num >= 0 and num < 11:
        print('el numero es entre 0 y 10 >>', num)
    elif num >= 11 and num < 50:
        print('el numero es entre 11 y 50 >> ', num)
    elif num >= 51 and num < 100:
        print('el numero es ente 50 y 100 >>', num)
    else:
        print('el numero es entre 100 y 120 >>', num)

numero()