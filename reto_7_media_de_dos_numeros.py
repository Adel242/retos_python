# Calcular la media de dos números.

def media():

    lista_num = [1, 2, 3,10]
    sum = 0

    for i in lista_num:
        sum = sum + i 
        media2 = sum / len(lista_num)
    print(media2)
    
media()

