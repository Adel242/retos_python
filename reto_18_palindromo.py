#  Dada una cadena decir si es un palíndromo.

p = input('escriba una palabra: ')
print('la palabra es: ', p)

length_p = len(p)

reversed_p = p[::-1]
print('reversed', reversed_p)
print('length', length_p)

print('la palabra al revez es: ', reversed_p)

if p == reversed_p:
    print('!!!FELICIDADES... esta palabra es un PALINDROMO')
else:
    print('esta es una palabra comun')
