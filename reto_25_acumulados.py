# Listar los números entre 1 y 10. En la columna contigua sus cuadrados, y en la tercera columna sus cubos. 
# Al final dar la suma de todos los valores de cada columna.

n_array = []
n_cuadrado_array = []
n_cubo_array = []

for n in range(0, 10):
    n_cuadrado = n **2
    n_cubo = n **3
    
    print(n, n_cuadrado, n_cubo)

    n_array.append(n)
    n_cuadrado_array.append(n_cuadrado)
    n_cubo_array.append(n_cubo)

    
print('suma de numeros', sum(n_array))
print('suma de numeros al cuadrado', sum(n_cuadrado_array))
print('suma de numeros al cubo', sum(n_cubo_array))

