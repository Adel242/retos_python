# Crear una función que calcule el Índice de Masa Corporal (Body Mass Index [BMI]).

peso = float(input('indique el peso de la persona en kilogramos: '))

estatura = float(input('indique la estatura de la persona en metros: '))

total = round(peso / estatura**2, 6)

print(total)

