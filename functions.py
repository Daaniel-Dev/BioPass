import json
from classes import *


def titulo(texto, linha='=', espacos=60, linha1=True, linha2=True):
    print(f'{linha}' * espacos) if linha1 else ''
    print(texto.center(espacos))
    print(f'{linha}' * espacos) if linha2 else ''


def menu(opcoes, mensagem='Escolha uma opção:'):
    print(mensagem)
    for i, opcao in enumerate(opcoes):
        print(f'[{i + 1}] {opcao}')
    while True:
        escolha = input()
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            return int(escolha) - 1
        else:
            print('\033[31;1mOpção inválida. Tente novamente.\033[m')


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
            with open(f'database/{nome}.json', 'w', encoding='utf-8') as arquivo:
                json.dump([], arquivo)
                continue


def editar_arquivo_json(objeto, nome_arq):
    dados = abrir_arquivo_json(nome_arq)
    dados.append(objeto.dados())
    with open(f'database/{nome_arq}.json', 'w', encoding='utf-8') as arquivo:
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
        elif len(cpf) == 11 and cpf.isnumeric():
            primeiro_digito = calcular_digito(cpf, True)
            segundo_digito = calcular_digito(cpf, False)
            dv_informado = cpf[9:]
            dv_calculado = str(primeiro_digito) + str(segundo_digito)
            if dv_informado == dv_calculado:
                cpf_existente = False
                dados = abrir_arquivo_json('dados')
                for usuario in dados:
                    if cpf == usuario["cpf"]:
                        cpf_existente = True
                        print('\033[31;1mCPF já cadastrado. Tente outro.\033[m')
                        break
                if not cpf_existente:
                    return cpf
            else:
                print('\033[31;1mCPF inválido. Tente novamente.\033[m')


def cadastro_senha():
    while True:
        senha = input('Digite uma senha: ').strip()
        if not senha.replace('@', '').isalnum():
            print('\033[31;1mCaractere(s) inválido(s), só é aceito o arroba (@). Tente novamente.\033[m')
            continue
        confirm = input('Confirme sua senha: ').strip()
        if senha == confirm:
            return senha
        else:
            print('\033[31;1mAs senhas não conferem. Tente novamente.\033[m')


def cadastro_usuario():
    cpf = cadastro_cpf()
    senha = cadastro_senha()
    nome = cadastro_nome()
    usuario = User(cpf, senha, nome)
    editar_arquivo_json(usuario, 'dados')
    print('\033[32;1mCadastro concluído com sucesso!\033[m')


def cadastro_nome_produto():
    while True:
        n = input('Nome do produto: ').strip().title()
        perg = menu(['Continuar', 'Digitar outro'], 'Deseja continuar ou digitar outro nome?')
        if perg == 1:
            continue
        else:
            return n


def cadastro_descricao_produto():
    while True:
        desc = input('Descrição do produto: ').strip()
        perg = menu(['Continuar', 'Digitar outra'], 'Deseja continuar ou digitar outra descrição?')
        if perg == 1:
            continue
        else:
            return desc


def cadastro_preco_produto():
    while True:
        try:
            prec = float(input('Preço do produto (R$): ').replace(',', '.'))
            perg = menu(['Continuar', 'Digitar outro'], 'Deseja continuar ou digitar outro preço?')
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
            if quant < 0:
                print('\033[31;1mValor abaixo de zero. Tente novamente.\033[m')
                continue
        except ValueError:
            print('\033[31;1mValor inválido. Tente novamente\033[m')
            continue
        perg = menu(['Continuar', 'Digitar outra'], 'Deseja continuar ou digitar outra quantidade?')
        if perg == 1:
            continue
        else:
            return quant


def cadastro_url_produto():
    while True:
        url = input('Link do vídeo (opcional): ').strip()
        if not url:
            return 'Não informado'
        else:
            pergunta = menu(['Continuar', 'Digitar outro'], 'Deseja continuar ou informar outro URL?')
            if pergunta == 1:
                continue
            else:
                return url


def cadastro_id_produto(dados):
    ids = [produto["id"] for produto in dados] if dados else []
    if ids:
        maior_id = max(ids)
        return maior_id + 1
    elif not ids:
        return 1


def cadastrar_produto(usuario):
    dados_produto = abrir_arquivo_json('produtos')
    id_produto = cadastro_id_produto(dados_produto)
    nome = cadastro_nome_produto()
    preco = cadastro_preco_produto()
    quantidade = cadastro_quantidade_produto()
    descricao = cadastro_descricao_produto()
    url_video = cadastro_url_produto()
    produto = Produto(usuario['cpf'], usuario['nome'], id_produto, nome,
                      preco, quantidade, descricao, url_video)
    dados_produto.append(produto.dados())
    with open(f'database/produtos.json', 'w', encoding='utf8') as arquivo:
        json.dump(dados_produto, arquivo, indent=1)
    print('\033[32;1mProduto cadastrado com sucesso!\033[m')


def listar_produtos_disponiveis(usuario, filtro=False):
    lista_produtos = abrir_arquivo_json('produtos')
    if filtro:
        lista_produtos = [produto for produto in lista_produtos if usuario["cpf"] == produto["cpf"]]
    if not lista_produtos:
        print('Nenhum produto disponível.')
    if lista_produtos:
        for indice, produto in enumerate(lista_produtos, start=1):
            if produto["quantidade"] >= 1:
                    titulo(f'Produto {indice}', '-')
                    print(f'''ID: {produto['id']}
Vendedor: {produto["nome do vendedor"]}
Produto: {produto["nome do produto"]}
Preço: R$ {produto['preço']:.2f}
Descrição: {produto['descrição']}
Quantidade: {produto['quantidade']}
URL: {produto["url"]}\n''')
    return lista_produtos


def comprar_produto(usuario):
    def percorrer_lista_produtos(lista, esc, acao, esc_quant=1):
        for produto in lista:
            if esc == produto["id"]:
                if acao == 1:
                    return produto
                elif acao == 2:
                    if esc_quant <= produto["quantidade"]:
                        produto["quantidade"] -= esc_quant
                    else:
                        print('\033[31;1mErro na compra. Quantidade solicitada maior que o estoque.\033[m')
                    return lista


    lista_produtos = abrir_arquivo_json('produtos')
    if not lista_produtos:
        print('Nenhum produto disponível.')
        return
    listar_produtos_disponiveis(usuario)
    while True:
        try:
            escolha = int(input('Digite o ID do produto que deseja comprar (0 para cancelar): '))
            if escolha == 0:
                print('\033[31;1mCompra cancelada.\033[m')
                return
            if 1 <= escolha <= len(lista_produtos):
                produto_escolhido = percorrer_lista_produtos(lista_produtos, escolha, 1)
                if produto_escolhido["cpf"] == usuario["cpf"]:
                    print('\033[31;1mVocê não pode comprar seu próprio produto.\033[m')
                    continue
                print(f'Você escolheu: {produto_escolhido["nome do produto"]} - '
                      f'R${produto_escolhido["preço"]}')
                confirmar = input('Deseja comprar? (S/N): ').strip().upper()
                if confirmar == 'S':
                    esc_quantidade = int(input('Deseja comprar quantas unidades? '))
                    if esc_quantidade > produto_escolhido['quantidade']:
                        print('\033[31;1mQuantidade maior que o estoque. Tente novamente.\033[m')
                        continue
                    cartao = input('Digite o número do cartão (fictício): ')
                    print(f'\033[32;1mCompra aprovada no cartão {cartao}!\033[m')
                    print(f'Obrigado por comprar {produto_escolhido["nome do produto"]}!')
                    nova_lista = percorrer_lista_produtos(lista_produtos, escolha, 2, esc_quantidade)
                    with open('database/produtos.json', 'w', encoding='utf8') as arquivo:
                        json.dump(nova_lista, arquivo, indent=1)
                else:
                    print('\033[31;1mCompra cancelada.\033[m')
                    return
            else:
                print('\033[31;1mProduto não encontrado.\033[m')
        except ValueError:
            print('\033[31;1mEntrada inválida.\033[m')


def funcao_depoimentos(usuario):
    dados_depoimentos = abrir_arquivo_json('depoimentos')
    while True:
        escolha = menu(['Adicionar Depoimento', 'Ver Depoimentos', 'Voltar'], 'Escolha uma opção:')
        if escolha == 0:
            nome = usuario["nome"]
            comentario = input('Seu depoimento: ').strip()
            if comentario:
                dados_depoimentos.append({"nome": nome, "comentario": comentario})
                with open(f'database/depoimentos.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(dados_depoimentos, arquivo, indent=1)
                print('\033[32;1mDepoimento adicionado com sucesso!\033[m')
            else:
                print('\033[31;1mDepoimento não pode ser vazio.\033[m')
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
    dados_video_educacional = abrir_arquivo_json('video_educacional')
    while True:
        escolha = menu(['Adicionar Link', 'Ver Links', 'Voltar'], 'Escolha uma opção:')
        if escolha == 0:
            link = input('Cole o link do seu vídeo educacional: ').strip()
            if link:
                link_existente = False
                for link_dados in dados_video_educacional:
                    if link_dados.find(link) != -1:
                        link_existente = True
                        print('\033[31;1mLink já cadastrado no sistema. Tente novamente.\033[m')
                if link_existente:
                    continue
                dados_video_educacional.append(link)
                with open('database/video_educacional.json', 'w') as arquivo:
                    json.dump(dados_video_educacional, arquivo, indent=1)
                print('\033[32;1mLink adicionado com sucesso!\033[m')
            else:
                print('\033[31;1mLink não pode estar vazio.\033[m')
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
        cpf = str(input('Digite seu CPF: ')).strip().replace('.', '').replace('-', '')
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
            if cpf == usuario['cpf'] and senha == usuario['senha']:
                print('\033[32;1mLogin concluído com sucesso!\033[m')
                return usuario
        print(f'\033[31;1mConta não encontrada ou os dados foram solicitados incorretamente. Tente novamente.\033[m')
        opcao = menu(['Continuar', 'Voltar'], 'O que deseja fazer?')
        if opcao == 0:
            continue
        elif opcao == 1:
            return 'Voltar'


def alterar_cadastro_usuario(usuario):
    def inf_alterar_usuario(lista, inf, inf_nova, arq):
        for usuarios_list in lista:
            if usuario["cpf"] == usuarios_list["cpf"]:
                usuarios_list[f"{inf}"] = inf_nova
        usuario[f"{inf}"] = inf_nova
        with open(f'database/{arq}.json', 'w', encoding='utf-8') as ARQUIVO:
            json.dump(lista, ARQUIVO, indent=1)


    while True:
        menu_opcoes = ['CPF', 'Senha', 'Nome', 'Voltar', 'Excluir conta']
        dados = abrir_arquivo_json('dados')
        produtos = abrir_arquivo_json('produtos')
        print(f'CPF: {usuario["cpf"]}\nSenha: {usuario["senha"]}\nNome: {usuario["nome"]}\n')
        alt_inf = menu(menu_opcoes, 'Deseja alterar qual informação?')
        if alt_inf == 0:
            cpf_novo = cadastro_cpf()
            inf_alterar_usuario(dados, 'cpf', cpf_novo, 'dados')
            inf_alterar_usuario(produtos, 'cpf', cpf_novo, 'produtos')
        elif alt_inf == 1:
            senha_nova = cadastro_senha()
            inf_alterar_usuario(dados, 'senha', senha_nova, 'dados')
        elif alt_inf == 2:
            nome_novo = cadastro_nome()
            inf_alterar_usuario(dados, 'nome', nome_novo, 'dados')
            inf_alterar_usuario(produtos, 'nome', nome_novo, 'produtos')
        elif alt_inf == 3:
            break
        elif alt_inf == 4:
            conf = menu(['Sim', 'Não'], 'Tem certeza de que deseja excluir sua conta? '
                                        '(Essa ação é irreversível)')
            if conf == 0:
                for dado in dados:
                    if dado["cpf"] == usuario["cpf"]:
                        dados.remove(dado)
                with open('database/dados.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, indent=1)
                for produto in produtos:
                    if produto["cpf"] == usuario["cpf"]:
                        produtos.remove(produto)
                with open('database/produtos.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(produtos,arquivo, indent=1)
                print('\033[32;1mConta excluida com sucesso!\033[m')
                return 'Conta excluída'
            elif conf == 1:
                continue
        print(f'\033[32;1m{menu_opcoes[alt_inf]} alterado(a) com sucesso!\033[m')


def alterar_cadastro_produto(usuario):
    def inf_alterar_produto(inf, inf_nova):
        for produto in produtos:
            if produto["cpf"] == usuario["cpf"] and escolha == produto["id"]:
                produto[f"{inf}"] = inf_nova
        with open('database/produtos.json', 'w', encoding='utf-8') as ARQUIVO:
            json.dump(produtos, ARQUIVO, indent=1)


    produtos_usuario = listar_produtos_disponiveis(usuario, True)
    while True:
        produtos = abrir_arquivo_json('produtos')
        if not produtos_usuario:
            print('Você não possui produtos cadastrados.')
            break
        try:
            lista_id = [produto['id'] for produto in produtos_usuario]
            escolha = int(input('Digite o ID do produto para alterar suas informações (0 para voltar):  '))
            if escolha in lista_id:
                menu_opcoes = ['Nome do produto', 'Descrição', 'Preço', 'Quantidade', 'URL', 'Voltar', 'Excluir produto']
                opcoes = menu(menu_opcoes, 'O que deseja alterar?')
                if opcoes == 0:
                    nome_novo = cadastro_nome_produto()
                    inf_alterar_produto('nome do produto', nome_novo)
                elif opcoes == 1:
                    desc_nova = cadastro_descricao_produto()
                    inf_alterar_produto('descrição', desc_nova)
                elif opcoes == 2:
                    preco_novo = cadastro_preco_produto()
                    inf_alterar_produto('preço', preco_novo)
                elif opcoes == 3:
                    quant_nova = cadastro_quantidade_produto()
                    inf_alterar_produto('quantidade', quant_nova)
                elif opcoes == 4:
                    url_nova = cadastro_url_produto()
                    inf_alterar_produto('url', url_nova)
                elif opcoes == 5:
                    break
                elif opcoes == 6:
                    conf = menu(['Sim', 'Não'], 'Tem certeza de que deseja excluir esse produto? '
                                                '(Essa ação é irreversível)')
                    if conf == 0:
                        for produto in produtos:
                            if produto["cpf"] == usuario["cpf"] and escolha == produto["id"]:
                                produtos.remove(produto)
                        with open('database/produtos.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(produtos, arquivo, indent=1)
                            print('\033[32;1mProduto excluído com sucesso!\033[m')
                    elif conf == 1:
                        continue
                print(f'\033[32;1m{menu_opcoes[opcoes]} alterado(a) com sucesso!\033[m')
            elif escolha not in lista_id:
                print('\033[31;1mID Inválido. Tente novamente.\033[m')
            elif escolha == 0:
                break
        except ValueError:
            print('\033[31;1mEntrada inválida.\033[m')
