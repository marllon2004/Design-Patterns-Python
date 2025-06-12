# iterator_produtos.py

# Classe Produto
class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto [ID: {self.id}, Nome: {self.nome}, Preço: R${self.preco:.2f}]"


# Classe ColecaoProdutos
class ColecaoProdutos:
    def __init__(self, reverso=False):
        self.produtos = []
        self.reverso = reverso

    def adicionar_produto(self, produto):
        """Adiciona um novo produto à coleção."""
        self.produtos.append(produto)

    def total_produtos(self):
        """Retorna o número total de produtos na coleção."""
        return len(self.produtos)

    def __iter__(self):
        """Retorna um iterador da coleção."""
        return IteradorProdutos(self.produtos, self.reverso)


# Classe IteradorProdutos
class IteradorProdutos:
    def __init__(self, produtos, reverso=False):
        self.produtos = produtos
        self.reverso = reverso
        self.posicao = len(produtos) - 1 if reverso else 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.reverso:
            if self.posicao < 0:
                raise StopIteration
            produto = self.produtos[self.posicao]
            self.posicao -= 1
            return produto
        else:
            if self.posicao >= len(self.produtos):
                raise StopIteration
            produto = self.produtos[self.posicao]
            self.posicao += 1
            return produto


# Exemplo de execução
if __name__ == "__main__":
    # Criação da coleção de produtos
    colecao = ColecaoProdutos()

    # Adicionando produtos
    colecao.adicionar_produto(Produto(1, 'Produto A', 29.99))
    colecao.adicionar_produto(Produto(2, 'Produto B', 49.99))
    colecao.adicionar_produto(Produto(3, 'Produto C', 19.99))

    print("\nIterando em ordem normal:")
    for produto in colecao:
        print(produto)

    print("\nIterando em ordem reversa:")
    colecao_reversa = ColecaoProdutos(reverso=True)
    colecao_reversa.adicionar_produto(Produto(1, 'Produto A', 29.99))
    colecao_reversa.adicionar_produto(Produto(2, 'Produto B', 49.99))
    colecao_reversa.adicionar_produto(Produto(3, 'Produto C', 19.99))

    for produto in colecao_reversa:
        print(produto)


"""
Explicação:
O padrão de projeto Iterator permite percorrer uma coleção de objetos sem expor sua estrutura interna. 
Ele separa a lógica de navegação da lógica da coleção em si, promovendo encapsulamento e flexibilidade. 
Ao usar um iterador personalizado, é possível estender facilmente a forma como os elementos são acessados (como ordem reversa), 
mantendo o código da coleção limpo e reutilizável.
"""
