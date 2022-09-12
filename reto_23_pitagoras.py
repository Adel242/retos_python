# Indicar las dimensiones de los triángulos rectángulos donde todas sus longitudes sean números enteros. 
# Listarlos hasta el límite donde los catetos lleguen hasta 100.

import math

for cateto_1 in range(1 ,101):
    for cateto_2 in range(cateto_1, 101): 
        hipotenusa = (cateto_1**2 + cateto_2**2)**.5
        if hipotenusa == int(hipotenusa):
            print('cateto 1:', cateto_1,'cateto 2:', cateto_2 ,'hipotenusa', hipotenusa,)

# uso de metodo mathipotenusa.sqrt para sacar raiz cuadrada

for cateto_1 in range(1, 101):
    for cateto_2 in range(cateto_1, 101):
        hipotenusa = math.sqrt(cateto_1**2 + cateto_2 **2)
        if hipotenusa == int(hipotenusa):
            print('cateto_1: ', cateto_1, 'cateto_2: ', cateto_2, 'hipotenusa: ',hipotenusa)

