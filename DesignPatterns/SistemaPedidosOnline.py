#Marllon Silva Araujo Coelho - 627021 - BCC

from abc import ABC, abstractmethod #caso as subclasses não implementem corretamente os métodos

class Produto(ABC):
    @abstractmethod
    def exibir_informacoes(self):
        pass

    @abstractmethod
    def adicionar_ao_pedido(self):
        pass

class Eletronico(Produto):
    def __init__(self, tipoProduto, preco, marca, quantidade):
        self.tipoProduto = tipoProduto
        self.preco = preco
        self.marca = marca
        self.quantidade = quantidade

    def exibir_informacoes(self):
        return f"Eletrônico: {self.tipoProduto} - {self.marca}, Preço: {self.preco}, Quantidade: {self.quantidade}"

    def adicionar_ao_pedido(self):
        return f"{self.tipoProduto} - {self.marca} foi adicionado ao carrinho."

class Roupa(Produto):
    def __init__(self, tipoProduto, marca, tamanho, cor, genero, quantidade):
        self.tipoProduto = tipoProduto
        self.marca = marca
        self.tamanho = tamanho
        self.cor = cor
        self.genero = genero
        self.quantidade = quantidade

    def exibir_informacoes(self):
        return f"Roupa: {self.tipoProduto} ({self.genero}) - {self.marca}, Tamanho: {self.tamanho}, Cor: {self.cor}, Quantidade: {self.quantidade}"

    def adicionar_ao_pedido(self):
        return f"{self.tipoProduto} ({self.genero}) - {self.marca} foi adicionado ao carrinho."

class Alimento(Produto):
    def __init__(self, tipoProduto, marca, peso, data_validade, quantidade):
        self.tipoProduto = tipoProduto
        self.marca = marca
        self.peso = peso
        self.data_validade = data_validade
        self.quantidade = quantidade

    def exibir_informacoes(self):
        return f"Alimento: {self.tipoProduto} ({self.peso}kg) - {self.marca}, Data de Validade: {self.data_validade}, Quantidade: {self.quantidade}"

    def adicionar_ao_pedido(self):
        return f"{self.tipoProduto} ({self.peso}kg) - {self.marca} foi adicionado ao pedido."

class Livro(Produto):
    def __init__(self, titulo, autor, editora, data_lancamento, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.data_lancamento = data_lancamento
        self.quantidade = quantidade

    def exibir_informacoes(self):
        return f"Livro: {self.titulo} - {self.autor}, Editora: {self.editora}, Data de Lançamento: {self.data_lancamento}, Quantidade: {self.quantidade}"

    def adicionar_ao_pedido(self):
        return f"{self.titulo} - {self.autor}, Editora: {self.editora} foi adicionado ao pedido."

class Brinquedo(Produto):
    def __init__(self, tipoBrinquedo, marca, preco, quantidade):
        self.tipoBrinquedo = tipoBrinquedo
        self.marca = marca
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informacoes(self):
        return f"Brinquedo: {self.tipoBrinquedo} - {self.marca}, Peso: {self.preco}, Quantidade: {self.quantidade}"

    def adicionar_ao_pedido(self):
        return f"{self.tipoBrinquedo} - {self.marca}, Preco: {self.preco}"

class ProdutoFactory:
    @staticmethod
    def criar_produto(tipo, **kwargs): #kwargs permite passarmos varios parametros com chaves e valores
        if tipo == "eletronico":
            return Eletronico(kwargs.get("tipoProduto"), kwargs.get("preco"), kwargs.get("marca"), kwargs.get("quantidade"))
        elif tipo == "roupa":
            return Roupa(kwargs.get("tipoProduto"), kwargs.get("marca"), kwargs.get("tamanho"), kwargs.get("cor"), kwargs.get("genero"), kwargs.get("quantidade"))
        elif tipo == "alimento":
            return Alimento(kwargs.get("tipoProduto"), kwargs.get("marca"), kwargs.get("peso"), kwargs.get("data_validade"), kwargs.get("quantidade"))
        elif tipo == "livro":
            return Livro(kwargs.get("titulo"), kwargs.get("autor"), kwargs.get("editora"), kwargs.get("data_lancamento"), kwargs.get("quantidade"))
        elif tipo == "brinquedo":
            return Brinquedo(kwargs.get("tipoBrinquedo"), kwargs.get("marca"), kwargs.get("preco"), kwargs.get("quantidade"))
        else:
            raise ValueError("Tipo de produto desconhecido.")


def simular_pedido():
    pedido = []

    eletronico = ProdutoFactory.criar_produto("eletronico", tipoProduto="Monitor", preco=854.05, marca="LG", quantidade=1)
    roupa = ProdutoFactory.criar_produto("roupa", tipoProduto="Camisa PSG", marca="Jordan", tamanho="L", cor="Roxa", genero="M", quantidade=2)
    alimento = ProdutoFactory.criar_produto("alimento", tipoProduto="Leite Fermentado", marca="Yakut", peso=0.850, data_validade="2025-12-31", quantidade=1)
    livro = ProdutoFactory.criar_produto("livro", titulo="Trono de Vidro", autor="Sarah J. Maas", editora="Galera", data_lancamento="2023-07-24", quantidade=1)
    brinquedo = ProdutoFactory.criar_produto('brinquedo', tipoBrinquedo="Transformes", marca="Hi Happy", preco=99.99, quantidade=3)

    pedido.append(eletronico.adicionar_ao_pedido())
    pedido.append(roupa.adicionar_ao_pedido())
    pedido.append(alimento.adicionar_ao_pedido())
    pedido.append(livro.adicionar_ao_pedido())
    pedido.append(brinquedo.adicionar_ao_pedido())

    for produto in pedido:
        print(produto)

simular_pedido()