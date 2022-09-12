#  Calcular cuantos granos de trigo tendríamos que utilizar si por cada casilla de un tablero de ajedrez (64 casillas)
# pusiéramos un grano en la primera casilla, dos en la segunda, cuatro en la tercera, y así doblando hasta la última.

def progresion_geometrica():
    num = 1
    for i in range(1, 65):
        num = num + i * 2
        print(i)
    print('las uma total de granos de trigo es: ', num)

progresion_geometrica()