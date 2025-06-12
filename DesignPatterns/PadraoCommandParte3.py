# Parte 2 - Extensões do Padrão Command

from abc import ABC, abstractmethod

# Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver com Dimmer
class Luz:
    def __init__(self, nome):
        self.nome = nome
        self.estado = False
        self.intensidade = 100

    def ligar(self):
        self.estado = True
        print(f"{self.nome} ligada com intensidade {self.intensidade}%.")

    def desligar(self):
        self.estado = False
        print(f"{self.nome} desligada.")

    def ajustar_intensidade(self, valor):
        anterior = self.intensidade
        self.intensidade = max(0, min(100, valor))
        print(f"Intensidade da {self.nome} ajustada de {anterior}% para {self.intensidade}%.")
        return anterior

# Concrete Commands
class LigarLuzCommand(Command):
    def __init__(self, luz):
        self.luz = luz

    def execute(self):
        self.luz.ligar()

    def undo(self):
        self.luz.desligar()

class DesligarLuzCommand(Command):
    def __init__(self, luz):
        self.luz = luz

    def execute(self):
        self.luz.desligar()

    def undo(self):
        self.luz.ligar()

class AjustarIntensidadeCommand(Command):
    def __init__(self, luz, nova_intensidade):
        self.luz = luz
        self.nova_intensidade = nova_intensidade
        self.intensidade_anterior = luz.intensidade

    def execute(self):
        self.intensidade_anterior = self.luz.ajustar_intensidade(self.nova_intensidade)

    def undo(self):
        self.luz.ajustar_intensidade(self.intensidade_anterior)

# Invoker
class ControleRemoto:
    def __init__(self):
        self.historico = []

    def executar_comando(self, comando):
        comando.execute()
        self.historico.append(comando)

    def desfazer_ultimo(self):
        if self.historico:
            comando = self.historico.pop()
            comando.undo()

# Cliente Controle de Luz com Dimmer
if __name__ == "__main__":
    luz_sala = Luz("Luz da Sala")

    ligar = LigarLuzCommand(luz_sala)
    ajustar = AjustarIntensidadeCommand(luz_sala, 50)
    desligar = DesligarLuzCommand(luz_sala)

    controle = ControleRemoto()
    controle.executar_comando(ligar)
    controle.executar_comando(ajustar)
    controle.executar_comando(desligar)
    controle.desfazer_ultimo()
    controle.desfazer_ultimo()


# Parte 2 - Editor de Texto com Histórico de Alterações

# Receiver
class EditorTexto:
    def __init__(self):
        self.texto = ""
        self.historico_alteracoes = []

    def adicionar_texto(self, novo_texto):
        self.texto += novo_texto
        self.historico_alteracoes.append(self.texto)
        print(f"Texto atual: {self.texto}")

    def remover_texto(self, quantidade):
        self.texto = self.texto[:-quantidade]
        self.historico_alteracoes.append(self.texto)
        print(f"Texto atual: {self.texto}")

    def exibir_historico(self):
        print("\nHistórico de Alterações:")
        for i, estado in enumerate(self.historico_alteracoes):
            print(f"{i + 1}: {estado}")

# Concrete Commands
class AdicionarTextoCommand(Command):
    def __init__(self, editor, texto):
        self.editor = editor
        self.texto = texto

    def execute(self):
        self.editor.adicionar_texto(self.texto)

    def undo(self):
        self.editor.remover_texto(len(self.texto))

# Invoker
class EditorInvoker:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def executar_comando(self, comando):
        comando.execute()
        self.undo_stack.append(comando)
        self.redo_stack.clear()

    def desfazer(self):
        if self.undo_stack:
            comando = self.undo_stack.pop()
            comando.undo()
            self.redo_stack.append(comando)

    def refazer(self):
        if self.redo_stack:
            comando = self.redo_stack.pop()
            comando.execute()
            self.undo_stack.append(comando)

# Cliente Editor com Histórico
if __name__ == "__main__":
    print("\nEditor de Texto com Histórico:")
    editor = EditorTexto()
    invoker = EditorInvoker()

    cmd1 = AdicionarTextoCommand(editor, "Era uma vez ")
    cmd2 = AdicionarTextoCommand(editor, "um editor de texto.")

    invoker.executar_comando(cmd1)
    invoker.executar_comando(cmd2)

    invoker.desfazer()
    invoker.refazer()

    editor.exibir_historico()


# Parte 3 - Novo Cenário: Sistema de Controle de Mídia

# Receiver
class Player:
    def __init__(self):
        self.estado = "Parado"

    def play(self):
        self.estado = "Reproduzindo"
        print("Player está reproduzindo.")

    def pause(self):
        self.estado = "Pausado"
        print("Player pausado.")

    def stop(self):
        self.estado = "Parado"
        print("Player parado.")

# Concrete Commands
class PlayCommand(Command):
    def __init__(self, player):
        self.player = player
        self.estado_anterior = player.estado

    def execute(self):
        self.estado_anterior = self.player.estado
        self.player.play()

    def undo(self):
        if self.estado_anterior == "Pausado":
            self.player.pause()
        elif self.estado_anterior == "Parado":
            self.player.stop()

class PauseCommand(Command):
    def __init__(self, player):
        self.player = player
        self.estado_anterior = player.estado

    def execute(self):
        self.estado_anterior = self.player.estado
        self.player.pause()

    def undo(self):
        if self.estado_anterior == "Reproduzindo":
            self.player.play()
        elif self.estado_anterior == "Parado":
            self.player.stop()

class StopCommand(Command):
    def __init__(self, player):
        self.player = player
        self.estado_anterior = player.estado

    def execute(self):
        self.estado_anterior = self.player.estado
        self.player.stop()

    def undo(self):
        if self.estado_anterior == "Reproduzindo":
            self.player.play()
        elif self.estado_anterior == "Pausado":
            self.player.pause()

# Invoker
class ControlePlayer:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def executar(self, comando):
        comando.execute()
        self.undo_stack.append(comando)
        self.redo_stack.clear()

    def desfazer(self):
        if self.undo_stack:
            comando = self.undo_stack.pop()
            comando.undo()
            self.redo_stack.append(comando)

    def refazer(self):
        if self.redo_stack:
            comando = self.redo_stack.pop()
            comando.execute()
            self.undo_stack.append(comando)

# Cliente Controle de Mídia
if __name__ == "__main__":
    print("\nControle de Mídia:")
    player = Player()
    controle = ControlePlayer()

    play_cmd = PlayCommand(player)
    pause_cmd = PauseCommand(player)
    stop_cmd = StopCommand(player)

    controle.executar(play_cmd)
    controle.executar(pause_cmd)
    controle.executar(stop_cmd)
    controle.desfazer()
    controle.refazer()
