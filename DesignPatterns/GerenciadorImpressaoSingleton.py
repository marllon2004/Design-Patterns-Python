#Marllon Silva Araujo Coelho - 627021

class GerenciadorDeImpressao:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._fila = []
        return cls._instance

    def __init__(self):
        pass

    def adicionar_documento(self, documento):
        self._fila.append(documento)
        print(f"Documento '{documento}' adicionado à fila.")

    def remover_documento(self, documento):
        if documento in self._fila:
            self._fila.remove(documento)
            print(f"Documento '{documento}' removido da fila.")
        else:
            print(f"Documento '{documento}' não encontrado na fila.")

    def mostrar_fila(self):
        if self._fila:
            print("Fila de impressão:", self._fila)
        else:
            print("A fila de impressão está vazia.")

gerenciador1 = GerenciadorDeImpressao()
gerenciador2 = GerenciadorDeImpressao()

assert gerenciador1 is gerenciador2, "Erro: As instâncias não são iguais!"
print("Ambas as instâncias são a mesma!")

gerenciador1.adicionar_documento("contrato_distrato.pdf")
gerenciador1.adicionar_documento("contrato_quitacao.docx")

gerenciador2.mostrar_fila()

gerenciador2.remover_documento("contrato_distrato.pdf")
gerenciador2.mostrar_fila()
