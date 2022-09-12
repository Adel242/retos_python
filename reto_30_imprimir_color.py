# Generar aleatoriamente la nota de diez alumnos. 
# Calcular la media e imprimir en pantalla la nota de cada uno y la desviación de cada una de las notas respecto a la media. 
# Los que estén por encima o por debajo de la media se imprimen en colores diferentes.

from random import randint

list_grades = []
list_reproved = []
list_approved = []

def average_grades():
    i = 0
    while i < 10:
        grades_random = randint(10, 70)
        if grades_random < 40:
            list_reproved.append(grades_random)
        if grades_random > 40:
            list_approved.append(grades_random)

        list_grades = list_approved + list_reproved
        average = sum(list_grades) / len(list_grades)
        i += 1

    for x in range(len(list_grades)):
        if list_grades[x] > average:
            print('desviacion con respecto a la nota media: ', round(list_grades[x] - average, 2), 'nota: ',list_grades[x])
        elif list_grades[x] < average: 
            print('desviacion con respecto a la nota media: ', round(list_grades[x] - average * -1, 2), 'nota: ', list_grades[x])

    print('\033[0;36m', 'notas totales', list_grades, '\033[0;m')
    print('\033[0;32m', 'alumnos aprobadas: ',list_approved,'\033[0;m')
    print('\033[0;31m', 'alumnos reprobados: ', list_reproved, '\033[0;m')
    print('\033[0;33m', 'promedio del curso: ', average,'\033[0;m')

average_grades()