alunos = ['Raphael', 7, 'Douglas', 7, 'Pedro', 8, 'Erica', 9.5]

dicionario = {}

for i, v in enumerate(alunos):
    if i % 2 == 0:
        dicionario.update({v: alunos[i+1]})    

while True:
    print('=' * 20)
    print('1. Consultar dicionário.')
    print('2. Atualizar uma nota.')
    print('3. Sair.')

    opcao = input('Escolha uma opção: ')
    if opcao == '3':
        print('Programa finalizado.')
        break  # Aqui encerramos o loop

    elif opcao == '1':
        print(f'Este é o dicionário: {dicionario}')
    
    elif opcao == '2':
        aluno = list(dicionario.keys())
        aluno_escolhido = input(f'Informe de qual aluno {aluno} gostaria de alterar a nota: ')
        while aluno_escolhido not in aluno:
            print('Aluno não está no dicionário. Tente novamente.')
            aluno_escolhido = input(f'Informe de qual aluno {aluno} gostaria de alterar a nota: ')
        nova_nota = float(input('Atualizar para qual nota? '))
        dicionario.update({aluno_escolhido: nova_nota})
    
    else:
        print('Opção inválida.')
