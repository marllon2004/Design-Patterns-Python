from abc import ABC, abstractmethod

# 1. Interface de Estratégia
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# 2. Estratégias Concretas

class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processando pagamento de R${amount:.2f} com Cartão de Crédito...")

class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processando pagamento de R${amount:.2f} com PayPal...")

class PIXPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processando pagamento de R${amount:.2f} via PIX...")

# 3. Classe Contexto

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def pay(self, amount):
        if not self._strategy:
            raise Exception("Nenhuma estratégia de pagamento definida.")
        self._strategy.process_payment(amount)

# 4. Simulação

if __name__ == "__main__":
    processor = PaymentProcessor()

    # Pagamento com Cartão de Crédito
    processor.set_strategy(CreditCardPayment())
    processor.pay(150.00)

    # Pagamento com PayPal
    processor.set_strategy(PayPalPayment())
    processor.pay(250.50)

    # Pagamento com PIX
    processor.set_strategy(PIXPayment())
    processor.pay(75.25)
