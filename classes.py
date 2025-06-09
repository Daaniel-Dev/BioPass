class User:
    def __init__(self, cpf, senha, nome):
        self.cpf = cpf
        self.senha = senha
        self.nome = nome
    def dados(self):
        return {"cpf": self.cpf, "senha": self.senha, "nome": self.nome}


class Produto:
    def __init__(self, cpf_vendedor, nome_vendedor, id_produto, nome_produto, preco, quantidade, descricao, url_video=''):
        self.cpf_vendedor = cpf_vendedor
        self.nome_vendedor = nome_vendedor
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.preco = preco
        self.descricao = descricao
        self.quantidade = quantidade
        self.url_video = url_video
    def dados(self):
        return {"cpf": self.cpf_vendedor, "id": self.id_produto, "nome do vendedor": self.nome_vendedor,
                "nome do produto": self.nome_produto, "preço": self.preco, "quantidade": self.quantidade,
                "descrição": self.descricao, "url": self.url_video}
