#  Crear una función que calcule el cuadrado de un número. Probar la función con los números entre -10 y +10. 
# Crear otra función que lo único que hace es imprimir al final la frase “Programa finalizado”. Ejecutar ambas funciones.

import math

def finalizado():
    print('Programa finalizado')

def cuadrado():

    for i in range(-10, 10):
        num = math.pow(i, 2)
        print(i, 'numero: ', num)
    
    finalizado()

cuadrado()

