class User:
    def __init__(self, cpf, senha, nome):
        self.cpf = cpf
        self.senha = senha
        self.nome = nome
    def dados(self):
        return {"cpf": self.cpf, "senha": self.senha, "nome": self.nome}


class Produto:
    def __init__(self, id_vendedor, nome_vendedor, nome_produto, preco, quantidade, descricao, url_video=''):
        self.id_vendedor = id_vendedor
        self.nome_vendedor = nome_vendedor
        self.nome_produto = nome_produto
        self.preco = preco
        self.descricao = descricao
        self.quantidade = quantidade
        self.url_video = url_video
    def dados(self):
        return {"id": self.id_vendedor, "nome do vendedor": self.nome_vendedor,
                "nome do produto": self.nome_produto, "preço": self.preco,
                "descrição": self.descricao, "quantidade": self.quantidade, "url": self.url_video}
        self.url_video = url_video

    def __str__(self):
        return (f'Produto: {self.nome}\nDescrição: {self.descricao}\nPreço: R${self.preco:.2f}\nVídeo: '
                f'{self.url_video if self.url_video else "Não informado"}')
