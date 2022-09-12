# Crear una función que detecte si dos palabras son anagramas.
def anagrama():
    p1 = input('ingrese una palabra: ')
    p2 = input('ingrese una segunda palabra: ')

    pa1 = list(p1)
    pa2 = list(p2)

    pa1.sort()
    pa2.sort()

    if pa1 == pa2:
        print('la palabra: ', p1, 'es anagrama de: ',p2)
    else:
        print('las palabras NO! son un anagrama')

anagrama()