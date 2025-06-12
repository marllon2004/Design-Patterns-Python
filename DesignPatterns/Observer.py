from abc import ABC, abstractmethod
from datetime import datetime

# 1. Interface Observer
class Observer(ABC):
    @abstractmethod
    def atualizar(self, publicacao):
        pass

# 2. Interface Subject (Observable)
class Subject(ABC):
    @abstractmethod
    def adicionar_seguidor(self, seguidor):
        pass

    @abstractmethod
    def remover_seguidor(self, seguidor):
        pass

    @abstractmethod
    def notificar_seguidores(self, publicacao):
        pass

# Classe de apoio para representar publicações
class Publicacao:
    def __init__(self, autor, conteudo):
        self.autor = autor
        self.conteudo = conteudo
        self.data_hora = datetime.now()

    def __str__(self):
        return f"{self.autor} publicou: '{self.conteudo}' em {self.data_hora.strftime('%d/%m/%Y %H:%M:%S')}"

# 3. Classe Usuario (Subject)
class Usuario(Subject):
    def __init__(self, nome):
        self.nome = nome
        self.seguidores = []

    def adicionar_seguidor(self, seguidor):
        if seguidor not in self.seguidores:
            self.seguidores.append(seguidor)

    def remover_seguidor(self, seguidor):
        if seguidor in self.seguidores:
            self.seguidores.remove(seguidor)

    def fazer_publicacao(self, texto):
        publicacao = Publicacao(self.nome, texto)
        print(str(publicacao))  # Mostra a publicação do autor
        self.notificar_seguidores(publicacao)

    def notificar_seguidores(self, publicacao):
        for seguidor in self.seguidores:
            seguidor.atualizar(publicacao)

# 4. Classe Seguidor (Observer)
class Seguidor(Observer):
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, publicacao):
        print(f"Seguidor {self.nome} recebeu notificação: {publicacao}")

# 5. Código de Teste
if __name__ == "__main__":
    # Criação dos usuários
    alice = Usuario("Alice")
    bob = Usuario("Bob")

    # Criação dos seguidores
    joao = Seguidor("João")
    maria = Seguidor("Maria")
    carla = Seguidor("Carla")

    # Seguidores seguem Alice
    alice.adicionar_seguidor(joao)
    alice.adicionar_seguidor(maria)

    # Seguidores seguem Bob
    bob.adicionar_seguidor(maria)
    bob.adicionar_seguidor(carla)

    print("\n--- Alice faz uma publicação ---")
    alice.fazer_publicacao("Hoje está um ótimo dia para programar!")

    print("\n--- Bob faz uma publicação ---")
    bob.fazer_publicacao("Novo vídeo no meu canal do YouTube!")

    print("\n--- Maria deixa de seguir Bob ---")
    bob.remover_seguidor(maria)

    print("\n--- Bob faz uma nova publicação ---")
    bob.fazer_publicacao("Postei um tutorial sobre o padrão Observer!")
