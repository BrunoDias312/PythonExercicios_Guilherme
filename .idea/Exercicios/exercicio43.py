valor = float(input('Digite o valor do item: '))
desconto = valor - (valor * 0.10)

comissao1 = desconto * 0.05
comissao1 = round(comissao1,2)

comissao2 = valor * 0.05
comissao2 = round(comissao2,2)

parcelado = valor / 3
parcelado = round(parcelado,2)

print(f'Total a pagar com desconto de 10%: R${desconto}')
print(f'O valor de cada parcela, no parcelamento de 3x sem juros: R${parcelado}')
print(f'Comissão do vendedor, no caso da venda ser a vista: R${comissao1}')
print(f'Comissão do vendedor, no caso da venda ser parcelada: R${comissao2}')
