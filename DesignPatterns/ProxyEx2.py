from abc import ABC, abstractmethod

class BankAccount(ABC):
    """Interface que define os métodos de depósito e saque."""
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class RealBankAccount(BankAccount):
    """Classe concreta que implementa os métodos de depósito e saque."""
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Depósito de {amount}. Novo saldo: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Saque de {amount}. Novo saldo: {self.balance}")
        else:
            print("Saldo insuficiente!")

class BankAccountProxy(BankAccount):
    """Proxy que adiciona segurança antes de permitir o acesso ao objeto real."""
    def __init__(self, real_account, user_role):
        self.real_account = real_account
        self.user_role = user_role  # O usuário deve ser um "admin" para realizar saques

    def deposit(self, amount):
        self.real_account.deposit(amount)

    def withdraw(self, amount):
        if self.user_role == "admin":
            self.real_account.withdraw(amount)
        else:
            print("Acesso negado! Apenas administradores podem realizar saques.")

# Demonstração
real_account = RealBankAccount(1000)
proxy = BankAccountProxy(real_account, user_role="user")

# Tentativa de saque com um usuário não autorizado
proxy.withdraw(200)  # Acesso negado!

# Mudando para um usuário autorizado
proxy.user_role = "admin"
proxy.withdraw(200)  # Saque bem-sucedido
