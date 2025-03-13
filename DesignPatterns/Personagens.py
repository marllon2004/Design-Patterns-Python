#Modelo disponibilizado para aula

# Primeiro, importamos algumas ferramentas especiais do Python que nos ajudam a criar "esboços" de classes.
from abc import ABC, abstractmethod

# Aqui, criamos um esboço para "Personagem". Pensando em jogos, personagens podem ser guerreiros, magos, etc.
class Personagem(ABC):
    # 'descrever' é como se fosse um comando para o personagem se apresentar, mas ainda não sabemos como ele fará isso.
    @abstractmethod
    def descrever(self):
        pass

    # 'equipar' é um comando para dar ao personagem algum equipamento, mas também não sabemos os detalhes ainda.
    @abstractmethod
    def equipar(self, equipamento):
        pass

# Este é outro esboço, mas para "Equipamento", como espadas ou escudos que os personagens podem usar.
class Equipamento(ABC):
    # 'nome' é para saber o nome do equipamento, mas ainda é só uma ideia geral.
    @abstractmethod
    def nome(self):
        pass

    # 'usar' é o que acontece quando o personagem usa o equipamento. Ainda é um mistério como isso funciona.
    @abstractmethod
    def usar(self):
        pass

# Mundo de fantasia
# Aqui, estamos criando um tipo específico de personagem chamado Guerreiro.
class Guerreiro(Personagem):
    # Quando pedimos ao Guerreiro para se descrever, ele diz que está pronto para a batalha.
    def descrever(self):
        return "Guerreiro pronto para a batalha!"

    # Quando equipamos o Guerreiro, ele anuncia o que está equipando.
    def equipar(self, equipamento):
        print(f"{self.descrever()} Equipando {equipamento.nome()}.")

# Este é um tipo de equipamento chamado Espada.
class Espada(Equipamento):
    # A Espada simplesmente diz seu nome quando perguntamos.
    def nome(self):
        return "Espada"

    # E o que a Espada faz? Ela ataca!
    def usar(self):
        return "Atacando com a espada!"

# Mundo futurista
# Agora, temos um tipo de personagem futurista chamado Soldado.
class Soldado(Personagem):
    # O Soldado, assim como o Guerreiro, tem sua própria descrição.
    def descrever(self):
        return "Soldado armado e pronto!"

    # E o Soldado também pode ser equipado, anunciando o que está equipando.
    def equipar(self, equipamento):
        print(f"{self.descrever()} Equipando {equipamento.nome()}.")

# Aqui está um tipo de equipamento futurista: o Rifle.
class Rifle(Equipamento):
    # O Rifle também tem um nome.
    def nome(self):
        return "Rifle"

    # E a ação que o Rifle faz é disparar.
    def usar(self):
        return "Disparando com o rifle!"

# A 'FabricaFantasia' é uma oficina especial onde podemos criar coisas do mundo de fantasia.
class FabricaFantasia(ABC):
    # Se precisarmos de um personagem desse mundo, a fábrica nos dará um Guerreiro.
    def criar_personagem(self):
        return Guerreiro()

    # E se precisarmos de um equipamento, a fábrica nos dará uma Espada.
    def criar_equipamento(self):
        return Espada()

# 'FabricaFuturista' é outra oficina, mas esta faz coisas de um futuro distante.
class FabricaFuturista(ABC):
    # Aqui, se pedirmos um personagem, recebemos um Soldado.
    def criar_personagem(self):
        return Soldado()

    # E para equipamento, a fábrica nos fornece um Rifle.
    def criar_equipamento(self):
        return Rifle()


# 'FabricaDeJogo' é como uma receita que diz o que deve ser feito, mas não como fazer.
# Ela é uma ideia geral para criar coisas num jogo, como personagens e equipamentos.
class FabricaDeJogo(ABC):
    # Aqui, temos uma "tarefa" que diz: "Você precisa ser capaz de criar um personagem."
    # Mas ainda não sabemos que tipo de personagem ou como ele será criado.
    @abstractmethod
    def criar_personagem(self):
        pass  # 'pass' é apenas uma maneira de dizer "nada acontece aqui".

    # Aqui, temos outra "tarefa" que diz: "Você também precisa ser capaz de criar equipamento."
    # Novamente, não sabemos o tipo de equipamento ou como ele será feito.
    @abstractmethod
    def criar_equipamento(self):
        pass  # Novamente, 'pass' significa que não há nada sendo feito aqui.

# Esta é uma função chamada 'cliente'. Ela é como um jogador que vai escolher seus personagens e equipamentos em um jogo.
# 'factory' é um lugar onde podemos fazer ou "fabricar" coisas, neste caso, personagens e equipamentos para o jogo.
def cliente(factory):
    # Aqui, pedimos à fábrica para criar um novo personagem para nós.
    personagem = factory.criar_personagem()
    # Depois, pedimos à fábrica para criar um equipamento para esse personagem.
    equipamento = factory.criar_equipamento()
    # Em seguida, dizemos ao personagem para usar (ou "equipar") o equipamento que acabamos de criar.
    personagem.equipar(equipamento)
    # Por fim, fazemos o equipamento realizar sua ação, como atacar ou disparar, e mostramos isso.
    print(equipamento.usar())

# Esta parte é como o início do jogo, onde tudo começa.
if __name__ == "__main__":
    # Primeiro, usamos a 'FabricaFantasia' para criar um personagem e equipamento do mundo de fantasia e vemos o que acontece.
    cliente(FabricaFantasia())
    print("---")  # Isso é apenas para separar os resultados na tela.
    # Depois, fazemos o mesmo, mas desta vez com a 'FabricaFuturista' para criar coisas do mundo futurista.
    cliente(FabricaFuturista())