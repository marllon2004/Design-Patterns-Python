#Marllon Silva Araujo Coelho - 627021

from abc import ABC, abstractmethod

#Classes abstratas
class Motor(ABC):
    @abstractmethod
    def tipo_motor(self):
        pass

class Veiculo(ABC):
    @abstractmethod
    def tipo_veiculo(self):
        pass

class Carro(Veiculo):
    def tipo_veiculo(self):
        return "Carro Terrestre"

class Aviao(Veiculo):
    def tipo_veiculo(self):
        return "Avião Aéreo"

class Barco(Veiculo):
    def tipo_veiculo(self):
        return "Barco Aquático"

class MotorCombustao(Motor):
    def tipo_motor(self):
        return "Motor a Combustão"

class MotorJato(Motor):
    def tipo_motor(self):
        return "Motor a Jato"

class MotorEletrico(Motor):
    def tipo_motor(self):
        return "Motor Elétrico"

#Fabrica Abstrata
class FabricaDeVeiculos(ABC):
    @abstractmethod
    def criar_veiculo(self):
        pass

    @abstractmethod
    def criar_motor(self):
        pass

#Fabricas Concretas
class FabricaTerrestre(FabricaDeVeiculos):
    def criar_veiculo(self):
        return Carro()

    def criar_motor(self):
        return MotorCombustao()

class FabricaAerea(FabricaDeVeiculos):
    def criar_veiculo(self):
        return Aviao()

    def criar_motor(self):
        return MotorJato()

class FabricaAquatica(FabricaDeVeiculos):
    def criar_veiculo(self):
        return Barco()

    def criar_motor(self):
        return MotorEletrico()

#Cliente
class Cliente:
    def __init__(self, fabrica: FabricaDeVeiculos):
        self.fabrica = fabrica
        self.veiculo = self.fabrica.criar_veiculo()
        self.motor = self.fabrica.criar_motor()

    def exibir_informações(self):
        print(f"Veículo: {self.veiculo.tipo_veiculo()}")
        print(f"Motor: {self.motor.tipo_motor()}")

def menu():
    print("Tipo de transporte:")
    print("1. Terrestre (Motor a Combustão)")
    print("2. Aéreo (Motor a Jato)")
    print("3. Aquático (Motor Elétrico)")

    opcao = input("Digite a opção desejada: ").strip()

    if opcao == "1":
        fabrica = FabricaTerrestre()
    elif opcao == "2":
        fabrica = FabricaAerea()
    elif opcao == "3":
        fabrica = FabricaAquatica()
    else:
        print("Opção inválida! Tente novamente.")
        return

    cliente = Cliente(fabrica)
    cliente.exibir_informações()

if __name__ == "__main__":
    while True:
        menu()
        continuar = input("\nDeseja escolher outro transporte? (s/n): ").strip().lower()
        if continuar != 's':
            print("Valeu! Encerrando...")
            break
