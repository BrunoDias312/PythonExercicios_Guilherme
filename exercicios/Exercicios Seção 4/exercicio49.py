hora_inicial = int(input('Digite a hora de inicio do experimento: '))
minutos_inicial = int(input('Digite os minutos: '))
segundos_inicial = int(input('Digite os segundos: '))
segundos_corridos = int(input('Digite o tempo de duração do experimento em segundos: '))

hora_final = hora_inicial + (segundos_corridos / 3600)
minutos_final = minutos_inicial + (segundos_corridos / 60)
segundos_final = segundos_inicial + segundos_corridos

print(f'Inicio do experimento {hora_inicial}:' f'{minutos_inicial}:' f'{segundos_inicial}')
print(f'Tempo de duração do experimento {segundos_corridos}s')
print(f'Final do experimento {hora_final}:' f'{minutos_final}:' f'{segundos_final}')

