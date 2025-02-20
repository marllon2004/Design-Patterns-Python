class Cliente: # Classe Cliente
    def exibir_informacoes(self):
        pass

class ClientePessoaFisica(Cliente): # Classe ClientePessoaFisica
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def exibir_informacoes(self):
        print(f"Cliente Pessoa Física: {self.nome}, CPF: {self.cpf}")

class ClientePessoaJuridica(Cliente): # Classe ClientePessoaJuridica
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj

    def exibir_informacoes(self):
        print(f"Cliente Pessoa Jurídica: {self.nome}, CNPJ: {self.cnpj}")

class ClientePessoaInternacional(Cliente): # Classe ClientePessoaInternacional
    def __init__(self, nome, nif):
        self.nome = nome
        self.nif = nif

    def exibir_informacoes(self):
        print(f"Cliente Pessoa Internacional: {self.nome}, NIF: {self.nif}")

    def validar_nif(self): # Método para validar o NIF
        if len(self.nif) > 9 and len(self.nif) < 12:
            return print('NIF válido!')
        print ('NIF inválido!')

class ClienteFactory:# Classe ClienteFactory
    # Metodo para criar um cliente
    def criar_cliente(self, tipo, nome, documento):
        if tipo == 'pessoa_fisica':
            return ClientePessoaFisica(nome, documento)
        elif tipo == 'pessoa_juridica':
            return ClientePessoaJuridica(nome, documento)
        elif tipo == 'pessoa_internacional':
            return ClientePessoaInternacional(nome, documento)
        else:
            raise ValueError("Tipo de cliente não suportado")

# Instanciando a fábrica
factory = ClienteFactory()

# Criando cliente do tipo Pessoa Física e exibindo informações
cliente_pf = factory.criar_cliente('pessoa_fisica', 'José Silva', '123.456.789-00')
cliente_pf.exibir_informacoes()

# Criando cliente do tipo Pessoa Juridica e exibindo informações
cliente_pj = factory.criar_cliente('pessoa_juridica', 'Empresa X', '98.765.432/0001-12')
cliente_pj.exibir_informacoes()

# Criando cliente do tipo Pessoa Internacional, exibindo informações e validando NIF
cliente_internacional = factory.criar_cliente('pessoa_internacional', 'Marllon', '12345678910')
cliente_internacional.exibir_informacoes()
cliente_internacional.validar_nif()

# Criando cliente do tipo Pessoa Internacional, exibindo informações e validando NIF
cliente_internacional_errado_nif = factory.criar_cliente('pessoa_internacional', 'Cliente sem NIF', '1598')
cliente_internacional_errado_nif.exibir_informacoes()
cliente_internacional_errado_nif.validar_nif()