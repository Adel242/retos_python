#  Crear una función que dado un año diga si es bisiesto.

def bisiesto():

    for i in range(2022):
        i + 1
        if i % 4 == 0:
            print('es un año bisiesto', i)
        else:
            print('año', i)

bisiesto()