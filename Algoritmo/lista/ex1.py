
import random

lista = [random.randint(1,20) for num in range(10)]

print(f'A lista é: {lista}')

# resposta com métodos nativos:
print(f'O maior número na lista é {max(lista)} e o menor é {min(lista)}.')

print('=-'*50)
# resposta encontrando maior e menor:
maior = menor = 0

for i, num in enumerate(lista):
    if i == 0:
        maior = menor = num
    
    if num >= maior:
        maior = num
    
    if num <= menor:
        menor = num

print(f'O maior número na lista é {maior} e o menor é {menor}.')