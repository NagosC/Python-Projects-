temperatura = lambda x: (x - 32) / 1.8

N1 = float(input('Digite a temperatura em Fahrenheit: '))

print(f'A temperatura em graus celcius é {temperatura(N1):.2f}')

