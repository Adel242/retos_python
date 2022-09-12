# Crear una serie de 10 palabras donde sus letras se obtienen de forma aleatoria. 
# Mostrar estas palabras y mostrar esas mismas palabras ordenadas alfabéticamente.

import random

def generate_random_word():

    list_vocal = ['a','e','i','o','u']
    list_consonante = ['b','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z',]
    i = 1

    new_word = ''
    while i < 4:
        word_vocal = random.choice(list_vocal)
        new_word += word_vocal 
        word_consonante = random.choice(list_consonante)
        new_word += word_consonante
        i += 1

    return new_word

txt = []

for x in range(10):
    txt.append(generate_random_word())

print(txt)


    