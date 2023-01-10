from math import pow
peso = float(input('Digite a sua massa: '))
altura = float(input('Digite a sua Altura: '))

bmi = lambda x,y: (x/pow(y,2))

print(f'O seu BMI é de {bmi(peso,altura):.2f}')
