import math

numero = float(input('Digite um numero: '))

if numero > 0:
    print(f'A raiz quadrada de {numero} é igual a', math.sqrt(numero))
else:
    print('Numero invalido')
