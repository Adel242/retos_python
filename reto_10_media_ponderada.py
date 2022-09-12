# Calcular la media ponderada de una serie de valores.

lista = [10, 20, 50, 70]

lista_2 = [0.10,0.25,0.25,0.40]

print('los pesos de suma 1?: ', sum(lista_2) == 1)

suma = 0

for i in lista:
    suma = suma + i
    media = suma / len(lista)

print('la nota aritmetica es: ', media)

# multiplicamos todos las notas por su respectiva ponderacion y luego sumamos los resultados

ponderada = 0
for x in range(len(lista)):
    ponderada = ponderada + lista[x] * lista_2[x]
print('la nota ponderada es :', ponderada)


