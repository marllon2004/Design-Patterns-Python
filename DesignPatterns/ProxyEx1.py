"""
A classe BankerProxy atualmente implementa um proxy para a classe BankerImpl, adicionando uma camada de segurança para verificar se o usuário está autorizado a realizar depósitos. Sua tarefa agora é estender o código para incluir um sistema de registro de logs (logging) que registre cada tentativa de saque. Este registro deve incluir o account_id, o amount solicitado e se o saque foi bem-sucedido ou não.
Requisitos:
Adicione um método de logging à classe BankerProxy que registre as informações mencionadas sempre que o método withdraw for chamado.
As informações de log devem ser registradas em um arquivo de texto chamado bank_transactions.log.
O log deve registrar a data e hora da tentativa de saque, o ID da conta, o valor solicitado, e se a transação foi bem-sucedida.
"""

import logging
from datetime import datetime
from abc import ABC, abstractmethod

# Configuração do logging
logging.basicConfig(
    filename='bank_transactions.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Banker(ABC):
    @abstractmethod
    def deposit(self, account_id, amount):
        pass

    @abstractmethod
    def withdraw(self, account_id, amount):
        pass


class BankerImpl(Banker):
    def deposit(self, account_id, amount):
        print(f"Depositando o valor {amount} na conta {account_id}")

    def withdraw(self, account_id, amount):
        print(f"Sacando o valor {amount} da conta {account_id}")
        return amount


class BankerProxy(Banker):
    def __init__(self):
        self._banker = BankerImpl()

    def deposit(self, account_id, amount):
        user_id = "banker"
        if user_id == "banker":
            self._banker.deposit(account_id, amount)
        else:
            raise PermissionError("O usuário atual não está autorizado a depositar.")

    def withdraw(self, account_id, amount):
        try:
            result = self._banker.withdraw(account_id, amount)
            success = True
        except Exception as e:
            result = None
            success = False
        # Log da operação
        logging.info(
            f"Tentativa de saque - Conta: {account_id}, Valor: {amount}, Sucesso: {success}"
        )
        return result


# Exemplo de uso
if __name__ == "__main__":
    proxy = BankerProxy()

    try:
        proxy.deposit("12345", 100)
    except PermissionError as e:
        print(e)

    print(proxy.withdraw("12345", 50))
