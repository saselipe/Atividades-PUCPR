from Formativa1 import tela_inicial, painel

def test_tela_inicial():
    msg = tela_inicial()
    assert "bem vindo ao sistema" in msg # checar se o painel está rodando
    assert "(1) Solicitar cartão" in msg # checar se fornece as opções

def test_painel_cartao():
    msg = painel(selecao=1) # se for 1 a seleção
    assert "solicitação de cartão" in msg # exibir corretamente
    assert "Mastercard" in msg # a opção

def test_painel_usuario_nome():
    msg = painel(selecao=2, funcao=1) # verificar se está funcionando corretamente a alteração do usuário
    assert "João da Silva" in msg

def test_painel_usuario_endereco(): # verificar se a opção "mudar endereço" está ok.
    msg = painel(selecao=2, funcao=2)
    assert "Rua Principal, 123" in msg

def test_painel_pix_cpf():
    msg = painel(selecao=3, funcao=1) # verificar se a mudança de chave pix está ok.
    assert "123.456.789-00" in msg

def test_painel_pix_email(): # verificar se a chave pix e-mail está ok
    msg = painel(selecao=3, funcao=2)
    assert "exemplo@email.com" in msg

def test_painel_invalido(): # se tentar acessar qualquer função fora das opções fornecidas pelo painel está ok
    msg = painel(selecao=99)
    assert "opção válida" in msg