valor = float(input('Digite o valor do produto: '))
valor_percentual = float(input('Digite o percentual de desconto: '))
desconto = valor - ((valor_percentual/100) * valor)

print(f'Valor com desconto: {desconto}')


