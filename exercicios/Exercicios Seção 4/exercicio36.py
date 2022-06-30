import math

altura = float(input('Digite a altura do cilindro: '))
raio = float(input('Digite o raio do cilindro: '))
pi = math.pi
volume = pi * (raio**2) * altura

print(f'Volume: {volume}.')
