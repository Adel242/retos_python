# Crear una aplicación que trabaje con la ley de capitalización compuesta.

cap_init = float(input('indique su capital inicial: '))

years = float(input('tiempo transcurrido en anos: '))

interes = float(input('ingrese el tipo de interes, si es del 5% ingrese 0.5: '))

print('capital inicial: ', cap_init)
print('dias transcurridos: ', years)
print('el interes es de: ', interes)

total = round(cap_init*(1 + interes)**years,2)

print('el total de dinero que tienes es: ', total)

