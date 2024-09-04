lista_tarefas = []

def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    if lista_tarefas:
        novo_id = max(tarefa['id'] for tarefa in lista_tarefas) + 1
    else:
        novo_id = 1

    nova_tarefa = {
        'id': novo_id,
        'descricao': descricao,
        'status': status,
        'prioridade': prioridade
    }

    lista_tarefas = lista_tarefas + [nova_tarefa]
    return lista_tarefas

def visualizar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Nenhuma tarefa para exibir.")
        return

    for tarefa in lista_tarefas:
        print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, "
              f"Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}")

def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    tarefas_filtradas = [
        tarefa for tarefa in lista_tarefas
        if (status is None or tarefa['status'] == status) and
           (prioridade is None or tarefa['prioridade'] == prioridade)
    ]
    return tarefas_filtradas

def menu():
    global lista_tarefas

    while True:
        print("\n---Gerenciamento de Tarefas---")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Filtrar Tarefas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            descricao = input("Descrição da tarefa: ").strip()
            status = input("Status da tarefa (pendente, em andamento, concluída): ").strip()
            prioridade = input("Prioridade da tarefa (alta, média, baixa): ").strip()
            lista_tarefas = adicionar_tarefa(lista_tarefas, descricao, status, prioridade)
        
        elif opcao == "2":
            visualizar_tarefas(lista_tarefas)
        
        elif opcao == "3":
            status = input("Filtrar por status (ou pressione Enter para ignorar): ").strip() or None
            prioridade = input("Filtrar por prioridade (ou pressione Enter para ignorar): ").strip() or None
            tarefas_filtradas = filtrar_tarefas(lista_tarefas, status=status, prioridade=prioridade)
            visualizar_tarefas(tarefas_filtradas)
        
        elif opcao == "4":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()












