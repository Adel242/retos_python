# generar matrices 3x3, 2x3 y 3x4
# ejemplo de matriz de 2x2
# [[1,1]
# [2,2]]

from random import randint

matrix = []

for i in range(10):
    matrix.append([])
    print('fila')
    for x in range(5):
        print('columna')
        
        matrix[i].append(randint(0,9))

for z in matrix:
    print(z) 
