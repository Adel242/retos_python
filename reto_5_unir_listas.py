#  Generar primero una lista con los números entre 0 y 10, luego generar otra lista con los números del 11 al 20. Unir ambas lista e imprimir el resultado.

lista_1 = []
lista_2 = []

for i in range(0, 10):
    lista_1.append(i)
print(lista_1)

for n in range(11, 20):
    lista_2.append(n)
print(lista_2)

lista_3 = lista_1 + lista_2

print(lista_3)