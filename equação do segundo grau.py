from math import sqrt, pow
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
a = int(input('Digite o valor de A: '))


raiz1 =  (-b + sqrt(pow(b, 2) -4 * a * c)) / 2 * a
raiz2 =  (-b - sqrt(pow(b, 2) -4 * a * c)) / 2 * a

print(f'O valor da raiz quadrada é de {raiz1} ou {raiz2}')
