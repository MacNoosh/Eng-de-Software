semana = {}

dias_da_semana = ('seg', 'ter', 'qua', 'qui', 'sex')

for dia in dias_da_semana:
    horas = float(input(f'Informe as horas trabalhadas na {dia}: '))
    semana.update({dia:horas})

horas = 0
for c, v in semana.items():
    print(f'{c}: {v}h')
    horas += v
print(f'Total de horas trabalhadas: {horas}h.')