valor_hora = float(input('Digite o valor da hora: '))
hora = float(input('Digite a quantidade de horas trabalhadas no mês: '))
salario = (valor_hora*hora) + ((valor_hora*hora)*0.10)

print(f'Salario a ser pago: R${salario}')
