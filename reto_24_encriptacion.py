# Encriptar y desencriptar frases usando la clave MURCIELAGO.
# Cada letra de la frase que coincida con alguna letra de la clave se sustituye por un número siguiendo el orden 0123456789.

clave = 'MURCIELAGO'

texto = input('escriba una palabra cualquiera: ').upper()

def encripar(txt):
    encriptado = ''
    for i in range(len(txt)):
        if txt[i] in clave:
            encriptado += str(clave.index(txt[i]))
        else:
            encriptado += txt[i]
    return encriptado


def desencriptar(txt):
    desencriptado = ''
    for x in range(len(txt)):
        if txt[x] in texto:
            desencriptado += str(texto.index(txt[x]))
        else:
            desencriptado += texto[x]

    return desencriptado

encript = encripar(texto)
print('el texto incriptado es: ', encripar(texto))
print('el texto desincriptado es: ', desencriptar(encript))

