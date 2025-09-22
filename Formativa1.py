def tela_inicial():
    return (
        "Olá, bem vindo ao sistema de gerenciamento do banco SIS!\n\n"
        "Você gostaria de acessar qual funcionalidade?\n"
        "(1) Solicitar cartão\n(2) Gerenciar usuário\n(3) Configurar chave(PIX)\n"
    )

def painel(selecao=1, funcao=1):
    if selecao == 1:
        cartao = 'Mastercard'
        return (
            "Você escolheu a solicitação de cartão!\n"
            "Em breve iremos te enviar a data de entrega do mesmo.\n"
            f"Seu cartão será bandeira {cartao}."
        )
    elif selecao == 2:
        if funcao == 1:
            nome = "João da Silva"
            return (
                "Você escolheu o gerenciamento de usuário!\n"
                "O que você deseja alterar?\n(1) Nome\n(2) Endereço\n"
                f"O nome atualizado é: {nome}"
            )
        elif funcao == 2:
            endereco = "Rua Principal, 123"
            return (
                "Você escolheu o gerenciamento de usuário!\n"
                "O que você deseja alterar?\n(1) Nome\n(2) Endereço\n"
                f"O endereço atualizado é: {endereco}"
            )
    elif selecao == 3:
        if funcao == 1:
            cpf = "123.456.789-00"
            return f"Sua chave (CPF) = {cpf}\n"
        elif funcao == 2:
            email = "exemplo@email.com"
            return f"Sua chave (E-mail) = {email}\n"
    else:
        return "Insira uma opção válida.\n"

if __name__ == "__main__":
    print(tela_inicial())
    print(painel())
