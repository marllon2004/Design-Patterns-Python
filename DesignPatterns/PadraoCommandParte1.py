# Parte 1 - Controle de Luzes

from abc import ABC, abstractmethod

# Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver
class Luz:
    def __init__(self, nome):
        self.nome = nome
        self.estado = False

    def ligar(self):
        self.estado = True
        print(f"{self.nome} ligada.")

    def desligar(self):
        self.estado = False
        print(f"{self.nome} desligada.")

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

# Cliente Controle de Luz
if __name__ == "__main__":
    luz_sala = Luz("Luz da Sala")

    ligar = LigarLuzCommand(luz_sala)
    desligar = DesligarLuzCommand(luz_sala)

    controle = ControleRemoto()
    controle.executar_comando(ligar)
    controle.executar_comando(desligar)
    controle.desfazer_ultimo()


# Parte 1 - Editor de Texto com Undo/Redo

# Receiver
class EditorTexto:
    def __init__(self):
        self.texto = ""

    def adicionar_texto(self, novo_texto):
        self.texto += novo_texto
        print(f"Texto atual: {self.texto}")

    def remover_texto(self, quantidade):
        self.texto = self.texto[:-quantidade]
        print(f"Texto atual: {self.texto}")

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

# Cliente Editor de Texto
if __name__ == "__main__":
    print("\nEditor de Texto:")
    editor = EditorTexto()
    invoker = EditorInvoker()

    cmd1 = AdicionarTextoCommand(editor, "Olá, ")
    cmd2 = AdicionarTextoCommand(editor, "mundo!")

    invoker.executar_comando(cmd1)
    invoker.executar_comando(cmd2)

    invoker.desfazer()
    invoker.refazer()
