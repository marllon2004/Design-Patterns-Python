from abc import ABC, abstractmethod

class ComponenteMissao(ABC):
    @abstractmethod
    def executar(self):
        pass

class TarefaSimples(ComponenteMissao):
    def __init__(self, nome):
        self.nome = nome

    def executar(self):
        print(f"Executando tarefa: {self.nome}")

class Missao(ComponenteMissao):
    def __init__(self, nome):
        self.nome = nome
        self.filhos = []

    def adicionar(self, componente: ComponenteMissao):
        self.filhos.append(componente)

    def remover(self, componente: ComponenteMissao):
        self.filhos.remove(componente)

    def executar(self):
        print(f"\nExecutando missão: {self.nome}")
        for filho in self.filhos:
            filho.executar()
        print(f"Finalizando missão: {self.nome}")

if __name__ == "__main__":
    # Criando tarefas simples
    tarefa1 = TarefaSimples("Lançar foguete")
    tarefa2 = TarefaSimples("Entrar em órbita da Terra")
    tarefa3 = TarefaSimples("Coletar amostras de solo lunar")
    tarefa4 = TarefaSimples("Transmitir dados para a Terra")
    tarefa5 = TarefaSimples("Ativar módulo de pouso")
    tarefa6 = TarefaSimples("Capturar imagens da superfície")

    #Missão secundária: Missão Lunar
    missao_lunar = Missao("Missão Lunar")
    missao_lunar.adicionar(tarefa1)
    missao_lunar.adicionar(tarefa2)
    missao_lunar.adicionar(tarefa3)

    #Missão secundária: Missão Marte
    missao_marte = Missao("Missão Marte")
    missao_marte.adicionar(tarefa1)
    missao_marte.adicionar(tarefa5)
    missao_marte.adicionar(tarefa6)
    missao_marte.adicionar(tarefa4)

    # Missão principal
    missao_principal = Missao("Exploração do Sistema Solar")
    missao_principal.adicionar(missao_lunar)
    missao_principal.adicionar(missao_marte)

    # Executando a missão principal
    missao_principal.executar()
