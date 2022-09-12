# Imprimir diez números aleatorios sin repetición entre 100 y 130, 
# excepto los números 110, 115, 120 y alternando par, impar, comenzando por par.

from random import randint

list_num = []
i = 0

while i < 9:
    num = randint(100, 130)
    if num not in list_num and num != 110 and num != 115 and num != 120:
        if num % 2 == 0 and i % 2 == 0:
            list_num.append(num)
            i += 1
        if num % 2 == 1 and i % 2 == 1 :
            list_num.append(num)
            i += 1

# list_num.sort()
print(list_num)
