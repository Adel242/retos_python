# Generar la tabla de multiplicar.

for i in range(1, 11):
    print('\n>>> Tabla del', i,)
    for x in range(1,11):
        r = x * i 
        print(i,'*',x,' = ',r,)