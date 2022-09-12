# Se genera un numero aletorio entero entre 1 y 100. El usuario debe adivinar el numero secreto, 
# diciendo en cada tirada si es mayor o menor

from random import randint

def numero_aletorio():

    while True:
        try:
            num = randint(1, 100)
            print('\n>> NUEVO NUMERO: ', num)
            select = int(input('escriba [1] si el siguiente numero es mayor, [2] si es menor o 3 si desea salir: '))
            print('seleccionaste: ',select)
            num2 = randint(1, 100)
            print('el numero es: ',num2)

            if num < num2 and select == 1:
                print('\n!!!ACERTASTE, el numero: ', num2 ,'es mayor que: ', num)
            elif num > num2 and select == 2:
                print('\n!!!ACERTASTE, el numero: ', num2, 'es menor: ', num)
            elif select == 3:
                print('Has salido del programa')
                break
            elif select != 1 and select != 2 and select != 3:
                print('\nSelecciona una opcion valida')
            else:
                print('\nno acertaste, vuelve a intentarlo')
        except ValueError:
            print('>> ERROR: escriba caracteres validos')
        
numero_aletorio()