from random import randint

matrix = []
matrix_2 = []
matrix_additions = []

print('Matrix 1')
for i in range(5):
    matrix.append([])
    for x in range(5):
        matrix[i].append(randint(0,9))

for z in matrix:
    print(z)

print('\nMatrix Reloaded')
for i in range(5):
    matrix_2.append([])
    for x in range(5):
        matrix_2[i].append(randint(0,9))

for z in matrix_2:
    print(z)

print('\nMatrix Additions')

for i in range(min(len(matrix), len(matrix_2))):
    matrix_additions.append(matrix[i]+matrix[i])
    
for x in matrix_additions:
    print(x)


