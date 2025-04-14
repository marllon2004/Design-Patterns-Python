#Marllon Silva Araujo Coelho - 627021

from abc import ABC, abstractmethod

class HamburgerBuilder(ABC):

    @abstractmethod
    def adicionar_pao(self):
        pass

    @abstractmethod
    def adicionar_carne(self):
        pass

    @abstractmethod
    def adicionar_queijo(self):
        pass

    @abstractmethod
    def adicionar_condimentos(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

class Hamburger:
    def __init__(self):
        self.ingredientes = []

    def add_ingredient(self, ingredient):
        self.ingredientes.append(ingredient)

    def __str__(self):
        return "Hambúrguer com " + ", ".join(self.ingredientes)

class ClassicHamburgerBuilder(HamburgerBuilder):
    def __init__(self):
        self.hamburger = Hamburger()

    def adicionar_pao(self):
        self.hamburger.add_ingredient("pão clássico")
        return self

    def adicionar_carne(self):
        self.hamburger.add_ingredient("carne de vaca")
        return self

    def adicionar_queijo(self):
        self.hamburger.add_ingredient("queijo cheddar")
        return self

    def adicionar_condimentos(self):
        self.hamburger.add_ingredient("maionese e ketchup")
        return self

    def get_result(self):
        return self.hamburger

class CheeseburgerBuilder(HamburgerBuilder):
    def __init__(self):
        self.hamburger = Hamburger()

    def adicionar_pao(self):
        self.hamburger.add_ingredient("pão de queijo")
        return self

    def adicionar_carne(self):
        self.hamburger.add_ingredient("carne de vaca")
        return self

    def adicionar_queijo(self):
        self.hamburger.add_ingredient("queijo gouda")
        return self

    def adicionar_condimentos(self):
        self.hamburger.add_ingredient("mostarda e ketchup")
        return self

    def get_result(self):
        return self.hamburger

class VeggieBurgerBuilder(HamburgerBuilder):
    def __init__(self):
        self.hamburger = Hamburger()

    def adicionar_pao(self):
        self.hamburger.add_ingredient("pão integral")
        return self

    def adicionar_carne(self):
        self.hamburger.add_ingredient("hambúrguer vegetal")
        return self

    def adicionar_queijo(self):
        self.hamburger.add_ingredient("queijo vegano")
        return self

    def adicionar_condimentos(self):
        self.hamburger.add_ingredient("molho de iogurte")
        return self

    def get_result(self):
        return self.hamburger

class ChickenBurgerBuilder(HamburgerBuilder):
    def __init__(self):
        self.hamburger = Hamburger()

    def adicionar_pao(self):
        self.hamburger.add_ingredient("pão de sésamo")
        return self

    def adicionar_carne(self):
        self.hamburger.add_ingredient("filé de frango grelhado")
        return self

    def adicionar_queijo(self):
        self.hamburger.add_ingredient("queijo provolone")
        return self

    def adicionar_condimentos(self):
        self.hamburger.add_ingredient("maionese picante")
        return self

    def get_result(self):
        return self.hamburger

class FishBurgerBuilder(HamburgerBuilder):
    def __init__(self):
        self.hamburger = Hamburger()

    def adicionar_pao(self):
        self.hamburger.add_ingredient("pão brioche")
        return self

    def adicionar_carne(self):
        self.hamburger.add_ingredient("filé de peixe empanado")
        return self

    def adicionar_queijo(self):
        self.hamburger.add_ingredient("queijo mozzarella")
        return self

    def adicionar_condimentos(self):
        self.hamburger.add_ingredient("molho tártaro")
        return self

    def get_result(self):
        return self.hamburger

class XTudoBuilder(HamburgerBuilder):
    def __init__(self):
        self.hamburger = Hamburger()

    def adicionar_pao(self):
        self.hamburger.add_ingredient("pão de cebola")
        return self

    def adicionar_carne(self):
        self.hamburger.add_ingredient("carne de vaca")
        return self

    def adicionar_queijo(self):
        self.hamburger.add_ingredient("queijo cheddar")
        return self

    def adicionar_condimentos(self):
        self.hamburger.add_ingredient("bacon crocante e barbecue")
        return self

    def get_result(self):
        return self.hamburger

class Chef:
    def __init__(self, builder):
        self.builder = builder

    def construir_hamburguer(self):
        return (self.builder
                .adicionar_pao()
                .adicionar_carne()
                .adicionar_queijo()
                .adicionar_condimentos()
                .get_result())

def main():
    builders = {
        '1': ClassicHamburgerBuilder(),
        '2': CheeseburgerBuilder(),
        '3': VeggieBurgerBuilder(),
        '4': ChickenBurgerBuilder(),
        '5': FishBurgerBuilder(),
        '6': XTudoBuilder()
    }

    while True:
        print("\nOpções de Hambúrguer:")
        print("1. Clássico")
        print("2. Cheeseburger")
        print("3. Vegetariano")
        print("4. Frango")
        print("5. Peixe")
        print("6. X tudo")
        print("7. Finalizar")

        choice = input("Escolha uma opção de hambúrguer ou '7' para finalizar: ")

        if choice == '7':
            print("Finalizado...")
            break

        if choice in builders:
            builder = builders[choice]
            chef = Chef(builder)
            hamburger = chef.construir_hamburguer()
            print("\n" + str(hamburger))
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
