numero = int(input('Informe um numero inteiro entre 100 e 999: '))


if numero >= 100 and numero <= 999:
    numero = str(numero)
    numero = "".join(reversed(numero))
    print(numero)
else:
    print('O numero informado não é um numero valido')
    