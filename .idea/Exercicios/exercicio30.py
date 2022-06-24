real = float(input('Digite seu saldo em R$: '))
cotação_dolar = float(input('Digite a cotação atual do $: '))

cambio = real / cotação_dolar
cambio = round(cambio, 2)

print(f'Saldo da carteira: R${real}')
print(f'Saldo da carteira convertido: ${cambio}')
