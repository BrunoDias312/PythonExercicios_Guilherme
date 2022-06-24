nota1 = input('Digite o resultado da primeira nota: ')
nota1 = float(nota1)

nota2 = input('Digite o resultado da segunda nota: ')
nota2 = float(nota2)

nota3 = input('Digite o resultado da terceira nota: ')
nota3 = float(nota3)

media_nota = (nota1 + nota2 + nota3) / 3
media_nota = float(media_nota)
media_nota = round(media_nota, 1)

print(f'A média das {nota1, nota2, nota3} é igual a' f' {media_nota}')
