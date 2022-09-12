# genera un numero aletorio y luego genera una lista de numeros aletorios en un rago de numeros
from random import randint, random

# numero aletorio
def aletorio(a, b):
    print('numero: ', randint(a, b))

aletorio(1 , 10)

# lista de numeros aletorios en un rango
def lista_num_aletorios(a, b):
    for i in range(10):
        i = i + 1
        print('numero ',i ,": ", randint(a, b))

lista_num_aletorios(1, 20)