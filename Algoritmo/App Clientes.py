clientes = []

def adicionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")

def exibir_clientes():
    for cliente in clientes:
        print(f'Nome: {cliente[0]}, Email: {cliente[1]},Telefone: {cliente[2]}, Endereço: {cliente[3]}')

def remover_clientes(email):
    for cliente in clientes:
        if cliente[1] == email:
            clientes.remove (cliente)
            print(f'Cliente com o Email {email} foi removido com sucesso !!!')
            return
    print('Cliente nao encontrado')
    
def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f'Nome: {cliente[0]}, Email: {cliente[1]},Telefone: {cliente[2]}, Endereço: {cliente[3]}')
            return
        print('Cliente nao encontrado')
        
#def testar():
   #adicionar_cliente('teste','teste','555555555555','rua de')
    #exibir_clientes('teste','teste','555555555555','rua de')

def menu():
    while True:
        print("\nSistema de Cadastro de Clientes")
        print("1. Adicionar Cliente")
        print("2. Exibir Clientes")
        print("3. Remover Cliente")
        print("4. Buscar Cliente por E-mail")
        print("5. Sair")
        #print("6. Testar")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            adicionar_cliente(nome, email, telefone, endereco)
        elif opcao =='2':
            exibir_clientes()
        elif opcao == '3':
            email = input("E-mail: ")
            remover_clientes(email)
        elif opcao == '4':
            email = input("E-mail: ")
            buscar_cliente(email)
        elif opcao == '5':
            print('saindo do programa')
        #elif opcao =='6':
            #testar()
            #break
        else:
            print('Opção inválida')
menu()
