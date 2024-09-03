clientes = []

def adicionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    clientes.append(cliente)
    print(f"Cliente {nome} adicionado com sucesso!")

def exibir_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for i, cliente in enumerate(clientes, start=1):
            nome, email, telefone, endereco = cliente
            print(f"Cliente {i}:")
            print(f" Nome: {nome}")
            print(f" E-mail: {email}")
            print(f" Telefone: {telefone}")
            print(f" Endereço: {endereco}")
            print("-" * 30)

def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            nome, email, telefone, endereco = cliente
            print("Cliente encontrado:")
            print(f" Nome: {nome}")
            print(f" E-mail: {email}")
            print(f" Telefone: {telefone}")
            print(f" Endereço: {endereco}")
            return cliente
    print("Cliente não encontrado.")
    return None

def remover_cliente(email):
    cliente = buscar_cliente(email)
    if cliente:
        clientes.remove(cliente)
        print(f"Cliente com e-mail {email} removido com sucesso!")
    else:
        print("Não foi possível remover o cliente.")

def menu():
    while True:
        print("\nSistema de Cadastro de Clientes")
        print("1. Adicionar Cliente")
        print("2. Exibir Clientes")
        print("3. Buscar Cliente por E-mail")
        print("4. Remover Cliente")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            adicionar_cliente(nome, email, telefone, endereco)
        elif opcao == '2':
            exibir_clientes()
        elif opcao == '3':
            email = input("Digite o e-mail do cliente que deseja buscar: ")
            buscar_cliente(email)
        elif opcao == '4':
            email = input("Digite o e-mail do cliente que deseja remover: ")
            remover_cliente(email)
        elif opcao == '5':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


menu()
