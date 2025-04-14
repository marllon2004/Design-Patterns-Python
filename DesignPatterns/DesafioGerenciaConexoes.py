#Marllon Silva Araujo Coelho - 627021

from abc import ABC, abstractmethod

#Abstract Product
class DataBase(ABC):
    @abstractmethod
    def tipo_conexao(self):
        pass

#Concrete Products
class ConexaoMysql(DataBase):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConexaoMysql, cls).__new__(cls)
        return cls._instance

    def tipo_conexao(self):
        return 'Conexão estabelecida com MySQL'

class ConexaoPostgreSql(DataBase):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConexaoPostgreSql, cls).__new__(cls)
        return cls._instance

    def tipo_conexao(self):
        return 'Conexão estabelecida com PostgreSQL'

class ConexaoSqlServer(DataBase):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConexaoSqlServer, cls).__new__(cls)
        return cls._instance

    def tipo_conexao(self):
        return 'Conexão estabelecida com SqlServer'

#Abstract Product
class StringConexao(ABC):
    @abstractmethod
    def obter_string(self):
        pass

#Concrete Products
class StringConexaoMysql(StringConexao):
    def obter_string(self):
        return 'mysql://root:senha@localhost:3306/banco'

class StringConexaoPostgreSql(StringConexao):
    def obter_string(self):
        return 'postgresql://root:senha@localhost:3308/banco'

class StringConexaoSqlServer(StringConexao):
    def obter_string(self):
        return 'mssql://root:senha@localhost:8001/banco'

#Abstract Factory
class FabricaBancoDados(ABC):
    @abstractmethod
    def criar_conexao(self) -> DataBase:
        pass

    @abstractmethod
    def criar_string_conexao(self) -> StringConexao:
        pass

#Concrete Factories
class FabricaMysql(FabricaBancoDados):
    def criar_conexao(self):
        return ConexaoMysql()

    def criar_string_conexao(self):
        return StringConexaoMysql()

class FabricaPostgreSql(FabricaBancoDados):
    def criar_conexao(self):
        return ConexaoPostgreSql()

    def criar_string_conexao(self):
        return StringConexaoMysql()

class FabricaSqlServer(FabricaBancoDados):
    def criar_conexao(self):
        return ConexaoSqlServer()

    def criar_string_conexao(self):
        return StringConexaoMysql()

#Código Cliente
class Cliente:
    def __init__(self, fabrica: FabricaBancoDados):
        self.fabrica = fabrica
        self.bancoDeDados = self.fabrica.criar_conexao()
        self.stringConexao = self.fabrica.criar_string_conexao()

    def exibir_informacoes(self):
        print(f"{self.bancoDeDados.tipo_conexao()}")
        print(f"String de conexão: {self.stringConexao.obter_string()}")
        print(f"Instância: {id(self.bancoDeDados)}")

#Menu interativo
def menu():
    print("--- Tipos de Conexões ---")
    print("1 - MySQL")
    print("2 - PostgreSQL")
    print("3 - SqlServer")

    opcao = input("Digite a opção desejada: ").strip()

    if opcao == "1":
        fabrica = FabricaMysql()
    elif opcao == "2":
        fabrica = FabricaPostgreSql()
    elif opcao == "3":
        fabrica = FabricaSqlServer()
    else:
        print("Opção inválida! Tente novamente.")
        return

    cliente = Cliente(fabrica)
    cliente.exibir_informacoes()

#Execução
if __name__ == "__main__":
    while True:
        menu()
        continuar = input("\nDeseja estabelecer outra conexão com o Banco de Dados? (s/n): ").strip().lower()
        if continuar != 's':
            print("Valeu! Encerrando...")
            break