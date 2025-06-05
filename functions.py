import json
from classes import *


def titulo(texto, linha='=', espacos=60):
    print(f'{linha}' * espacos)
    print(texto.center(espacos))
    print(f'{linha}' * espacos)


def menu(opcoes, mensagem='Escolha uma opção:'):
    print(mensagem)
    for i, opcao in enumerate(opcoes):
        print(f'[{i + 1}] {opcao}')
    while True:
        escolha = input()
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            return int(escolha) - 1
        else:
            print('Opção inválida. Tente novamente.')


def sobre():
    titulo('SOBRE NÓS')
    print('''Este é um aplicativo simples para compra e venda de produtos sustentáveis. 
Os usuários podem se cadastrar como clientes ou vendedores. 
Vendedores podem cadastrar produtos, enquanto os clientes podem adquiri-los. 
Nosso objetivo é ser um marketplace que permita tanto grandes quanto pequenos vendedores divulgar seus produtos, 
oferecendo a plataforma ideal para o reconhecimento de seus talentos. 
Além disso, o app permite que usuários e vendedores adicionem vídeos sobre seus produtos. 
Há também uma seção educativa para orientar os usuários sobre como reutilizar ou descartar itens sem utilidade.''')


def cadastro_nome():
    while True:
        nome = input('Digite seu nome: ').strip().title()
        if nome:
            return nome
        else:
            print('Nome inválido. Tente novamente.')


def abrir_arquivo_json(nome):
    while True:
        try:
            with open(f'database/{nome}.json', 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                return dados
        except FileNotFoundError:
            with open(f'database/{nome}.json', 'w', encoding='utf-8') as arquivo:
                json.dump([], arquivo)
                continue
        except json.JSONDecodeError:
            with open(f'database/{nome}.json', 'w') as arquivo:
                json.dump([], arquivo)
                continue


def editar_arquivo_json_objeto(objeto, nome):
    dados = abrir_arquivo_json(nome)
    dados.append(objeto.dados())
    with open(f'database/{nome}.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=1)


def cadastro_cpf():
    def calcular_digito(cpf_inf, digito1=True):
        numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        somatorio = 0
        for conjunto in zip(cpf_inf, numeros[1:] if digito1 else numeros):
            somatorio += int(conjunto[0]) * conjunto[1]
        resto_digito = somatorio % 11
        resto_digito = 0 if resto_digito == 10 else resto_digito
        return resto_digito

    while True:
        cpf = str(input('Cadastre seu CPF: ')).strip().replace('.', '').replace('-', '')
        if len(cpf) != 11 or not cpf.isnumeric():
            print('\033[31;1mCPF inválido. É necessário 11 dígitos numéricos.\033[m')
        else:
            primeiro_digito = calcular_digito(cpf, True)
            segundo_digito = calcular_digito(cpf, False)
            dv_informado = cpf[9:]
            dv_calculado = str(primeiro_digito) + str(segundo_digito)
            if dv_informado == dv_calculado:
                dados = abrir_arquivo_json('dados')
                for usuario in dados:
                    for dado in usuario:
                        if cpf == dado['cpf']:
                            print('\033[31;1mCPF já cadastrado. Tente outro.\033[m')
                            break
                    else:
                        return cpf
            else:
                print('\033[31;1mCPF inválido. Tente novamente.\033[m')


def cadastro_senha():
    while True:
        senha = input('Digite uma senha: ').strip()
        confirm = input('Confirme sua senha: ').strip()
        if senha == confirm:
            print('\033[32;1mSenha cadastrada com sucesso!\033[m')
            return senha
        else:
            print('\003[31;1mAs senhas não conferem. Tente novamente.\033[m')


def cadastro_usuario():
    cpf = cadastro_cpf()
    senha = cadastro_senha()
    nome = cadastro_nome()
    usuario = User(cpf, senha, nome)
    editar_arquivo_json_objeto(usuario, 'dados')
    print('\033[32;1mCadastro concluído com sucesso!\033[m')


def cadastrar_produto(usuario):
    def cadastro_nome_produto():
        while True:
            n = input('Nome do produto: ').strip().title()
            preg = menu(['CONTINUAR', 'DIGITAR OUTRO'], 'Deseja continuar ou digitar outro nome?')
            if preg == 1:
                continue
            else:
                return n


    def cadastro_descricao_produto():
        while True:
            desc = input('Descrição do produto: ').strip()
            perg = menu(['CONTINUAR', 'DIGITAR OUTRA'], 'Deseja continuar ou digitar outra descrição?')
            if perg == 1:
                continue
            else:
                return desc


    def cadastro_preco_produto():
        while True:
            try:
                prec = float(input('Preço do produto (R$): ').replace(',', '.'))
                perg = menu(['CONTINUAR', 'DIGITAR OUTRO', 'Deseja continuar ou digitar outro preço?'])
                if perg == 1:
                    continue
                else:
                    return prec
            except ValueError:
                print('\033[31;1mValor inválido. Tente novamente\033[m')


    def cadastro_quantidade_produto():
        while True:
            try:
                quant = int(input('Unidades do produto: '))
            except ValueError:
                print('\033[31;Valor inválido. Tente novamente\033[m')
            perg = menu(['CONTINUAR', 'DIGITAR OUTRA'], 'Deseja continuar ou digitar outra quantidade?')
            if perg == 1:
                continue
            else:
                return quant


    def cadastro_url_produto():
        while True:
            url = input('Link do vídeo (opcional): ').strip()
            if not url:
                'Não informado'
            else:
                pergunta = menu(['CONTINUAR', 'DIGITAR OUTRO'], 'Deseja continuar ou informar outro URL?')
                if pergunta == 1:
                    continue
                else:
                    return url

    nome = cadastro_nome_produto()
    preco = cadastro_preco_produto()
    quantidade = cadastro_quantidade_produto()
    descricao = cadastro_descricao_produto()
    url_video = cadastro_url_produto()
    produto = Produto(usuario['cpf'], usuario['nome'], nome, preco, quantidade, descricao, url_video)
    dados_produto = abrir_arquivo_json('produtos')
    dados_produto.append(produto.dados())
    with open(f'produtos.json', 'w') as arquivo:
        json.dump(dados_produto, arquivo, indent=2)
    print('\033[32;1mProduto cadastrado com sucesso!\033[m')


def listar_produtos_disponiveis():
    lista_produtos = abrir_arquivo_json('produtos')
    if not lista_produtos:
        print('Nenhum produto disponível.')
    else:
        for produto in lista_produtos:
            for caracteristicas in produto:
                if caracteristicas["quantidade"] >= 1:
                    titulo(f'Produto {caracteristicas["id"]}', '-')
                    print(f'''Vendedor: {caracteristicas["nome do vendedor"]}
    Produto: {caracteristicas["nome do produto"]}
    Preço {caracteristicas['preço']}
    Descrição: {caracteristicas['descrição']}
    Quantidade: {caracteristicas['quantidade']}
    URL: {caracteristicas["url"]}\n''')


def comprar_produto():
    def percorrer_lista(lista, esc, acao):
        for produto in lista:
            for detalhes in produto:
                if esc == detalhes["id"]:
                    if acao == 1:
                        return detalhes
                    elif acao == 2:
                        detalhes["quantidade"] -= 1
                        return lista
    lista_produtos = abrir_arquivo_json('produtos')
    if not lista_produtos:
        print('Nenhum produto disponível.')
        return
    listar_produtos_disponiveis()
    try:
        escolha = int(input('Digite o número do produto que deseja comprar (0 para cancelar): '))
        if escolha == 0:
            print('Compra cancelada.')
            return
        if 1 <= escolha <= len(lista_produtos):
            produto_escolhido = percorrer_lista(lista_produtos, escolha, 1)
            print(f'Você escolheu: {produto_escolhido["nome do produto"]} - '
                  f'R${produto_escolhido["preço"]}')
            confirmar = input('Deseja comprar? (S/N): ').strip().upper()
            if confirmar == 'S':
                cartao = input('Digite o número do cartão (fictício): ')
                print(f'Compra aprovada no cartão {cartao}!')
                print(f'Obrigado por comprar {produto_escolhido["nome do produto"]}!')
                nova_lista = percorrer_lista(lista_produtos, escolha, 2)
                with open('database/produtos.json', 'w') as arquivo:
                    json.dump(nova_lista, arquivo, indent=1)
            else:
                print('Compra cancelada.')
        else:
            print('Produto não encontrado.')
    except ValueError:
        print('Entrada inválida.')


def funcao_depoimentos():
    while True:
        escolha = menu(['Adicionar Depoimento', 'Ver Depoimentos', 'Voltar'], 'Escolha uma opção:')
        if escolha == 0:
            nome = input('Seu nome: ').strip().title()
            comentario = input('Seu depoimento: ').strip()
            if comentario:
                dados_depoimentos = abrir_arquivo_json('depoimentos')
                dados_depoimentos.append({"nome": nome, "comentario": comentario})
                with open(f'database/depoimentos.json', 'w') as arquivo:
                    json.dump(dados_depoimentos, arquivo, indent=1)
                print('Depoimento adicionado com sucesso!')
            else:
                print('Depoimento não pode ser vazio.')
        elif escolha == 1:
            if not dados_depoimentos:
                print('Nenhum depoimento ainda.')
            else:
                print('\n--- Depoimentos ---\n')
                for d in dados_depoimentos:
                    print(f'{d["nome"]} disse: "{d["comentario"]}"\n')
        else:
            break


def video_educacional():
    while True:
        escolha = menu(['Adicionar Link', 'Ver Links', 'Voltar'], 'Escolha uma opção:')
        if escolha == 0:
            link = input('Cole o link do seu vídeo educacional: ').strip()
            if link:
                dados_video_educacional = abrir_arquivo_json('video_educacional')
                dados_video_educacional.append(link)
                with open('database/video_educacional') as arquivo:
                    json.dump(dados_video_educacional, arquivo, indent=1)
                print('Link adicionado com sucesso!')
            else:
                print('Link não pode estar vazio.')
        elif escolha == 1:
            if not dados_video_educacional:
                print('Nenhum link cadastrado.')
            else:
                print('\n--- Vídeos Educacionais ---')
                for i, link in enumerate(dados_video_educacional, start=1):
                    print(f'{i}. {link}')
                print()
        else:
            break


def login_cpf():
    while True:
        cpf = str(input('Digite seu CPF: ')).strip().replace('.', '')
        if len(cpf) != 11 or not cpf.isnumeric():
            print('\033[31;1mCPF inválido. É necessário 11 dígitos numéricos.\033[m')
        else:
            return cpf


def login_senha():
    senha = input('Digite sua senha: ').strip()
    return senha


def login_usuario():
    while True:
        cpf = login_cpf()
        senha = login_senha()
        dados = abrir_arquivo_json('dados')
        for usuario in dados:
            for dado in usuario:
                if cpf == dado['cpf'] and senha == dado['senha']:
                    return dado
        print(f'\033[31;1mConta não encontrada ou os dados foram solicitados incorretamente. Tente novamente.\033[m')
        opcao = menu(['Continuar', 'Voltar'], 'O que deseja fazer?')
        if opcao == 0:
            continue
        elif opcao == 1:
            return 'Voltar'
