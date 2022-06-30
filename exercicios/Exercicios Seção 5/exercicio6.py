numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

if numero1 > numero2:
    print(f'Maior numero: {numero1}')
    print(f'Diferença entre {numero1} e' f' {numero2}:', numero1 - numero2)

else:
    print(f'Maior numero: {numero2}')
    print(f'Diferença entre {numero2} e' f' {numero1}:', numero2 - numero1)
