import math

numero = float(input('Digite um numero: '))

if numero > 0:
    print(f'A raiz quadrada de {numero} é', math.sqrt(numero))

else:
    print(f'{numero} ao quadrado é', numero ** 2)
