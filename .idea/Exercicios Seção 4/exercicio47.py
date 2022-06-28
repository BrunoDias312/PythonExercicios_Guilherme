numero = int(input('Digite um numero de 1000 a 9999: '))

if numero >= 1000 and numero<= 9999:
    numero = str(numero)
    print(numero[0])
    print(numero[1])
    print(numero[2])
    print(numero[3])
else:
    print('Esse não é um numero valido')
