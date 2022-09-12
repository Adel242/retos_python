# Generar un número aleatorio entero entre un millón y dos millones. Imprimir ese número en pantalla y decir cuántas cifras pares e impares tiene.

from random import randint

def numbers():
    num = randint(1e6, 2e6)
    num_str= str(num)
    print('el numero es: ', num)
    
    count_p = 0
    count_i = 0

    for i in num_str:
        x = int(i)
        if x % 2 == 0:
            print('el numero: ', x, 'es par')
            count_p += 1
        else:
            print('el numero: ', x,'es impar')
            count_i += 1

    print('Hay ', count_p, ' numeros pares')
    print('Hay ', count_i, 'numeros impares')
    
numbers()