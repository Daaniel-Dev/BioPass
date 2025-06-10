from functions import *

esp = 65
titulo('BioPass - Seu marketplace de produtos sustentáveis!', espacos=esp)
try:
    while True:
        opcao1 = menu(['Login', 'Cadastrar', 'Sair'])
        if opcao1 == 0:
            usuario = login_usuario()
            if usuario == 'Voltar':
                continue
            titulo(f'Seja bem vindo(a), {usuario['nome']}!', '-', esp, linha2=False)
            while True:
                print('-' * esp)
                opcao2 = menu(['Ver produtos disponíveis', 'Comprar produto', 'Cadastrar produto',
                               'Alterar informações de cadastro', 'Alterar informações do seu produto' ,'Depoimentos',
                                'Vídeos educacionais', 'Finalizar sessão'])
                if opcao2 == 0:
                    listar_produtos_disponiveis(usuario)
                elif opcao2 == 1:
                    comprar_produto(usuario)
                elif opcao2 == 2:
                    cadastrar_produto(usuario)
                elif opcao2 == 3:
                    resultado_cadastro_usuario = alterar_cadastro_usuario(usuario)
                    if resultado_cadastro_usuario == 'Conta excluída':
                        usuario = None
                        break
                elif opcao2 == 4:
                    alterar_cadastro_produto(usuario)
                elif opcao2 == 5:
                    funcao_depoimentos(usuario)
                elif opcao2 == 6:
                    video_educacional()
                elif opcao2 == 7:
                    print('Finalizando sessão...')
                    break
        elif opcao1 == 1:
            usuario = cadastro_usuario()
        elif opcao1 == 2:
            break
except KeyboardInterrupt:
    print('\nInterrompendo programa...')
print('\033[1mObrigado por usar nosso app!\033[m')
