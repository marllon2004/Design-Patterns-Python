#Marllon Silva Araujo Coelho - 627021

from abc import ABC, abstractmethod

#1. Interface Builder
class ConstrutorCasa(ABC):
    @abstractmethod
    def construir_fundacao(self):
        pass

    @abstractmethod
    def construir_estrutura(self):
        pass

    @abstractmethod
    def construir_telhado(self):
        pass

    @abstractmethod
    def pintar_casa(self):
        pass

    @abstractmethod
    def mobiliar_casa(self):
        pass

    @abstractmethod
    def get_casa(self):
        pass


#2. Construtores Concretos
class ConstrutorCasaModerna(ConstrutorCasa):
    def __init__(self):
        self.casa = Casa()

    def construir_fundacao(self):
        self.casa.add('Fundação moderna')

    def construir_estrutura(self):
        self.casa.add('Estrutura moderna com janelas amplas')

    def construir_telhado(self):
        self.casa.add('Telhado plano')

    def pintar_casa(self):
        self.casa.add('Pintura branca')

    def mobiliar_casa(self):
        self.casa.add('Móveis minimalistas')

    def get_casa(self):
        return self.casa

class ConstrutorCasaDeCampo(ConstrutorCasa):
    def __init__(self):
        self.casa = Casa()

    def construir_fundacao(self):
        self.casa.add('Fundação de pedra')

    def construir_estrutura(self):
        self.casa.add('Estrutura de madeira com ambientes aconchegantes')

    def construir_telhado(self):
        self.casa.add('Telhado em duas águas')

    def pintar_casa(self):
        self.casa.add('Cores pastéis')

    def mobiliar_casa(self):
        self.casa.add('Móveis estilo vintage')

    def get_casa(self):
        return self.casa

#Novo Construtor Casa de Netherite
class ConstrutorCasaNetherite(ConstrutorCasa):
    def __init__(self):
        self.casa = Casa()

    def construir_fundacao(self):
        self.casa.add('Fundação de netherite')

    def construir_estrutura(self):
        self.casa.add('Estrutura de netherite e vidro')

    def construir_telhado(self):
        self.casa.add('Telhado de obsidiana')

    def pintar_casa(self):
        self.casa.add('Pintura roxa')

    def mobiliar_casa(self):
        self.casa.add('Quadros de creeper e vasos de flor')

    def get_casa(self):
        return self.casa


#3. Produto
class Casa:
    def __init__(self):
        self.partes = []

    def add(self, parte):
        self.partes.append(parte)

    def descrever(self):
        return ', '.join(self.partes)


#4. Diretor
class DiretorDeConstrucao:
    def __init__(self, construtor):
        self._construtor = construtor

    def construir_casa(self):
        self._construtor.construir_fundacao()
        self._construtor.construir_estrutura()
        self._construtor.construir_telhado()
        self._construtor.pintar_casa()
        self._construtor.mobiliar_casa()
        return self._construtor.get_casa()

    #Metodo de construir casa padrão
    def construir_casa_padrao(self):
        self._construtor.construir_fundacao()
        self._construtor.construir_estrutura()
        self._construtor.construir_telhado()
        self._construtor.pintar_casa()
        return self._construtor.get_casa()

    #Metodo de construir casa personalizada
    def construir_casa_personalizada(self, tipo_material):
        self._construtor.construir_fundacao()
        self._construtor.construir_estrutura()
        if tipo_material == 'sustentavel':
            self._construtor.construir_telhado()  #Telhado ecológico
        else:
            self._construtor.construir_telhado()  #Telhado convencional
        self._construtor.pintar_casa()
        return self._construtor.get_casa()


#5. Utilizando o Código

if __name__ == "__main__":
    construtor_moderno = ConstrutorCasaModerna()
    diretor = DiretorDeConstrucao(construtor_moderno)
    casa = diretor.construir_casa()
    print(f"Casa Moderna: {casa.descrever()}")

    construtor_campo = ConstrutorCasaDeCampo()
    diretor = DiretorDeConstrucao(construtor_campo)
    casa = diretor.construir_casa()
    print(f"Casa de Campo: {casa.descrever()}")

    # Novo tipo de casa: Netherite
    construtor_luxo = ConstrutorCasaNetherite()
    diretor = DiretorDeConstrucao(construtor_luxo)
    casa = diretor.construir_casa()
    print(f"Casa de Netherite: {casa.descrever()}")

    # Construção de casa personalizada
    construtor_personalizado = ConstrutorCasaModerna()
    diretor = DiretorDeConstrucao(construtor_personalizado)
    casa = diretor.construir_casa_personalizada('sustentavel')
    print(f"Casa Personalizada Sustentável: {casa.descrever()}")
