import copy

# Classe Texto representa o conteúdo de um documento
class Texto:
    def __init__(self, conteudo=""):
        # Inicializa o conteúdo do texto com um valor padrão vazio
        self.conteudo = conteudo

    def adicionar(self, texto):
        # Adiciona um novo texto ao conteúdo existente
        self.conteudo += texto

    def clone(self):
        # Cria uma cópia profunda do objeto atual, essencial para implementar o Undo/Redo
        return copy.deepcopy(self)

    def __str__(self):
        # Retorna o conteúdo atual como uma string
        return self.conteudo

# Classe Editor gerencia o texto e o histórico de ações (Undo/Redo)
class Editor:
    def __init__(self):
        # Estado atual do texto
        self.estado_atual = Texto()
        # Lista para armazenar os estados anteriores (histórico de ações para desfazer)
        self.historico = []
        # Lista para armazenar os estados futuros (ações que podem ser refeitas)
        self.futuro = []

    def escrever(self, texto):
        # Adiciona um novo texto ao estado atual e armazena o estado anterior para permitir o Undo
        self.historico.append(self.estado_atual.clone())  # Armazena o estado atual antes de modificar
        self.estado_atual.adicionar(texto)  # Modifica o estado atual

    def desfazer(self):
        # Desfaz a última ação (retorna ao estado anterior)
        if self.historico:
            # Salva o estado atual para possível refazer
            self.futuro.append(self.estado_atual.clone())
            # Restaura o estado anterior
            self.estado_atual = self.historico.pop()

    def refazer(self):
        # Refaz a última ação desfeita (volta ao estado futuro)
        if self.futuro:
            # Armazena o estado atual para possível desfazer novamente
            self.historico.append(self.estado_atual.clone())
            # Restaura o estado futuro
            self.estado_atual = self.futuro.pop()

    def __str__(self):
        # Retorna o conteúdo atual do texto como string
        return str(self.estado_atual)

# Exemplo de uso do Editor e suas funcionalidades de Undo/Redo
editor = Editor()

# Escrevendo no editor
editor.escrever("Primeira frase. ")
editor.escrever("Segunda frase. ")

print(editor)

# Realizando a ação de desfazer (Undo)
editor.desfazer()
print(editor)

# Realizando mais uma ação de desfazer (Undo)
editor.desfazer()
print(editor)

# Realizando a ação de refazer (Redo)
editor.refazer()
print(editor)

# Realizando a ação de refazer novamente (Redo)
editor.refazer()
print(editor)