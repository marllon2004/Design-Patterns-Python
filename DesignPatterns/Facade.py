# Subsistema: Gerenciamento de Catálogo de Livros
class CatalogManager:
    def __init__(self):
        self.books = {}

    """Adiciona um livro ao catálogo."""
    def add_book(self, book_id, details):
        self.books[book_id] = details
        print(f"Livro adicionado: {details}")

    """Remove um livro do catálogo."""
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"Livro {book_id} removido")
        else:
            print("Livro não encontrado")

    """Busca um livro no catálogo."""
    def find_book(self, book_id):
        return self.books.get(book_id, "Livro não encontrado")


# Subsistema: Gerenciamento de Pedidos
class OrderManager:
    def __init__(self):
        self.orders = []

    """Cria um novo pedido."""
    def create_order(self, book_id, user_id):
        order = {"book_id": book_id, "user_id": user_id}
        self.orders.append(order)
        print(f"Pedido criado para o livro {book_id} pelo usuário {user_id}")


# Subsistema: Processamento de Pagamentos
class PaymentProcessor:
    """Processa um pagamento para um determinado usuário."""
    def process_payment(self, user_id, amount):
        print(f"Pagamento de R${amount:.2f} processado para o usuário {user_id}")


# Classe Facade
class BookstoreFacade:
    def __init__(self):
        self.catalog = CatalogManager()
        self.orders = OrderManager()
        self.payments = PaymentProcessor()

    """Realiza um pedido completo, incluindo verificação de livro, criação de pedido e pagamento."""
    def place_order(self, book_id, user_id, price):
        book = self.catalog.find_book(book_id)
        if book != "Livro não encontrado":
            self.orders.create_order(book_id, user_id)
            self.payments.process_payment(user_id, price)
            print("Pedido realizado com sucesso!\n")
        else:
            print("Livro indisponível\n")


# Código Cliente
if __name__ == "__main__":
    facade = BookstoreFacade()

    # Adiciona livros ao catálogo
    facade.catalog.add_book(1, "Dom Casmurro")
    facade.catalog.add_book(2, "Bíblia")
    facade.catalog.add_book(3, "Torto Arado")

    # Tenta fazer pedidos
    facade.place_order(1, 101, 39.90)
    facade.place_order(2, 102, 29.90)
    facade.place_order(4, 103, 49.90)  # Livro inexistente
