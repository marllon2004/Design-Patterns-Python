#Marllon Silva Araujo Coelho - 627021

from abc import ABC, abstractmethod
from datetime import datetime

# Interface comum
class Mensagem(ABC):
    @abstractmethod
    def exibir(self) -> str:
        pass

# Componente concreto
class MensagemBasica(Mensagem):
    def exibir(self) -> str:
        return "Olá"

# Decorator base
class MensagemDecorator(Mensagem):
    def __init__(self, mensagem: Mensagem):
        self._mensagem = mensagem

    @abstractmethod
    def exibir(self) -> str:
        pass

# Decorator concreto - adiciona nome
class MensagemComNome(MensagemDecorator):
    def __init__(self, mensagem: Mensagem, nome: str):
        super().__init__(mensagem)
        self._nome = nome

    def exibir(self) -> str:
        return f"{self._mensagem.exibir()}, {self._nome}"

# Decorator concreto - adiciona emoji
class MensagemComEmoji(MensagemDecorator):
    def __init__(self, mensagem: Mensagem, emoji: str = "😊"):
        super().__init__(mensagem)
        self._emoji = emoji

    def exibir(self) -> str:
        return f"{self._mensagem.exibir()} {self._emoji}"

# Decorator concreto - saudação baseada na hora do dia
class MensagemComSaudacaoPorHorario(MensagemDecorator):
    def exibir(self) -> str:
        hora = datetime.now().hour
        if hora < 12:
            saudacao = "Bom dia"
        elif hora < 18:
            saudacao = "Boa tarde"
        else:
            saudacao = "Boa noite"
        return f"{saudacao}! {self._mensagem.exibir()}"

if __name__ == "__main__":
    mensagem = MensagemBasica()
    mensagem = MensagemComNome(mensagem, "Marllon")
    mensagem = MensagemComEmoji(mensagem, "🚀")
    mensagem = MensagemComSaudacaoPorHorario(mensagem)

    print(mensagem.exibir())
