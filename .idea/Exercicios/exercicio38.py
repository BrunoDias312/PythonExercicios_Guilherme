salario = float(input('Digite o valor do salario: '))
percentual_salario = float(input('Digite o percentual de aumento: '))
aumento = salario + ((percentual_salario / 100) * salario)

print(f'Salario atual: R${salario}')
print(f'Salario após aumento: R${aumento}')
