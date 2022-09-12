# Crear una función que calcule la longitud de una cadena alfanumérica. 
# Crear otra función que dada una cadena devuelva el primer caracter en mayúsculas y el resto en minúsculas.
# Pasar una palabra por ambas funciones y dar el resultado.

def string(p):
    return len(p)

def uppercase():
    return palabra.capitalize()

palabra = input('\nescriba una palabra alfanumerica cualquiera: ')
print('la palabra es: ', palabra ,'\n')

print('la palabra', uppercase(), 'tiene', string(palabra), 'caracteres\n')
