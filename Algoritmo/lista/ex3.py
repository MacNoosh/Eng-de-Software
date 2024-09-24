import random


numericos = [random.randint(1,30)for num in range(10)]

def calculo_media(numericos):
    soma = 0
    for num in numericos:
        soma += num

    media = soma / len(numericos)
    return media

resultado = calculo_media(numericos)

print(f'A lista é {numericos} e sua média é {resultado}')
