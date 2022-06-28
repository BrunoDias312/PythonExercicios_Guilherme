salario_base = float(input('Informe o salario base: '))
salario_receber = (salario_base + (salario_base*0.05)) - (salario_base*0.07)
salario_receber = round(salario_receber,2)

print(f'Salario a receber: R${salario_receber}')

