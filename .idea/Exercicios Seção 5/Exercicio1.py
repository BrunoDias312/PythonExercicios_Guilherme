numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

if numero1 > numero2:
    print(f'{numero1} é maior do que' f' {numero2}')

elif numero1 == numero2:
    print('O primeiro numero informado é igual ao segundo numero informado')

else:
    print(f'{numero2} é maior do que o' f' {numero1}')