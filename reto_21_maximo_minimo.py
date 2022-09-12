# Generar 10 números aleatorios y calcular el máximo y el mínimo.

from random import randint

def max_min():
    num_arr = []
    i = 0

    while i < 10:
        num = randint(1, 10)
        num_arr.append(num)
        i += 1

    print('los numeros son: ',num_arr)
    num_arr.sort()

    print('el numero minimo es: ', num_arr[0])
    print('el numero maximo es: ', num_arr[9])
  
max_min()

