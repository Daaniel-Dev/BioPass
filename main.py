from functions import *

espacos = 65
titulo('Ecora - Seu marketplace de produtos sustentáveis!', espacos=espacos)
while True:
    opcao1 = menu(['Login', 'Cadastrar', 'Sair'])
    if opcao1 == 0:
        usuario = login_usuario()
        if usuario == 'Voltar':
            continue
        titulo(f'Seja bem vindo, {usuario['nome']}!', '-', espacos)
        while True:
            print('-' * espacos)
            opcao2 = menu(['Ver produtos disponíveis', 'Comprar produto', 'Cadastrar produto', 'Depoimentos',
                      'Vídeos educacionais', 'Finalizar sessão'])
            if opcao2 == 0:
                listar_produtos_disponiveis()
            elif opcao2 == 1:
                comprar_produto()
            elif opcao2 == 2:
                cadastrar_produto(usuario)
            elif opcao2 == 3:
                funcao_depoimentos()
            elif opcao2 == 4:
                video_educacional()
            elif opcao2 == 5:
                print('Finalizando sessão...')
                break
    elif opcao1 == 1:
        usuario = cadastro_usuario()
    elif opcao1 == 2:
        print('Obrigado por usar nosso app.')
        break
