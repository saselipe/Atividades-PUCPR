def tela_inicial():
    print("Olá, bem vindo ao sistema de gerenciamento do banco SIS!\n\n")
    print("Você gostaria de acessar qual funcionalidade?\n(1) Solicitar cartão\n(2) Gerenciar usuário\n(3) Configurar chave(PIX)\n")
    painel()

def painel():
    selecao = int(input("Inserir funcionalidade, apenas digite o número indicado.\n"))
    if selecao == 1:
        print("Você escolheu a solicitação de cartão!\nEm breve iremos te enviar a data de entrega do mesmo.")
        cartao = 'Mastercard'
        print(f'Seu cartão será bandeira {cartao}. ')
    elif selecao == 2:
        print("Você escolheu o gerenciamento de usuário!\nO que você deseja alterar?\n(1) Nome\n(2) Endereço")
        funcao = int(input())
        if funcao == 1:
            nome = input("Insira o nome: ")
            print(f'O nome atualizado é: {nome}')
        elif funcao == 2:
            endereco = input("Insira o endereço: ")
            print(f'O endereço atualizado é: {endereco}')

tela_inicial()