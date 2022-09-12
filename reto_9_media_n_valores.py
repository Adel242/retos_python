# Calcular la media de n números.

def media():

    numeros = []
    sum = 0

    while True:

        c = int(input('escribe la cantidad  de numeros: '))

        for i in range(c):
            num = int(input('escribe los numeros: '))
            numeros.append(num)
            sum = num + sum  
            media = sum / len(numeros)

        print(numeros)
        print(media)

        break

media()
