# Generar números aleatorios pares entre 100 y 130, salvo 110 y 120.

from random import randint


list_numbers = []
i = 1

while i < 10:
    num = randint(100, 131)
    if num % 2 == 0 and num != 110 and num != 120:
        list_numbers.append(num)
        i += 1

print(list_numbers)