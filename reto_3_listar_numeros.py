# Listar los números del 1 al 10.

from random import randint


def listar_num():
    print('>>>> lista de numeros del 1 al 10')
    for i in range(1,10):
        print(i)

listar_num()

# Listar los números pares del 10 al 20.

def listar_num_pares():
    print('\n>>>>> lista de numeros pares entre 10 y 20')
    for i in range(10, 21):
        if i % 2 == 0:
            print(i)

listar_num_pares()

# Listar los números entre un valor inicial y uno final, con un cierto intervalo. Al final dar la suma de todos los valores listados.

def listar_suma_num(a, b):
    print('\n>>>> lista de suma de numeros')
    num = 0
    for i in range(1, 50):
        if i % 5 == 0:
            num = num + i
            print(i)

    print('total: ', num)
listar_suma_num(10, 20)
