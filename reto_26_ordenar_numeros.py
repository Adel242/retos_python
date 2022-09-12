# Imprimir una lista de 10 números aleatorios sin repetición que varíen en el rango 80 a 99. 
# Volver a imprimir la lista pero ordenada.

from random import randint

lista_numeros = []
i = 1

while i < 10:
    num = randint(80, 99)
    if num not in lista_numeros:
        lista_numeros.append(num)
        i = i + 1

print(lista_numeros)
lista_numeros.sort()
print(lista_numeros)
