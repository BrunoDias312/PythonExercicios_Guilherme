nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if nota1 and nota2 >= 0 and nota1 and nota2 <= 10 :
    print('Média das notas: ', (nota1 + nota2) / 2)

else:
    print('O valor informado não é valido')


