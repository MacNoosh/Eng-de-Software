frutas = []

for i in range(5):
    nova_fruta = input('Digite uma fruta: \n')
    frutas.append(nova_fruta)

fruta = input('Informa uma fruta para verificar se a mesma esta na ssua lista: \n')

if fruta in frutas:
    print(f'{fruta} está na sua lista')
else:
    print(f'{fruta} não está na lista')
