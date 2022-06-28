import math

a = float(input('Digite o valor de "A": '))
b = float(input('Digite o valor de "b": '))
hipotenusa = (a**2) + (b**2)
raiz_hipotenusa = math.sqrt(hipotenusa)

print(f'A hipotenusa do triangulo é {raiz_hipotenusa}')
