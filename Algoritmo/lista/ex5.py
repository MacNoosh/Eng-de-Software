lista = []

for i in range(5):
    num = int(input('Acrescente um número à lista: '))
    lista.append(num)

lista_unica = list(dict.fromkeys(lista))

print(f'Lista original: {lista}\nLista sem repetições: {lista_unica}')
