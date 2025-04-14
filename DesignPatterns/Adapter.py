#Marllon Silva Araujo Coelho - 627021

#Interface de Notificação
class NotificationInterface:
    def send(self, message):
        """Método para enviar uma mensagem."""
        pass

#Criação das classes Adapters
class EmailService:
    def send_email(self, subject, body):
        """Método específico para enviar emails."""
        print(f"Enviando email - Assunto: {subject}, Corpo: {body}")

#2. Implementação de Novos Adapters
class SMSService:
    def send_sms(self, number, message):
        print(f"Enviando SMS para {number}: {message}")

class TwitterService:
    def post_tweet(self, message):
        print(f"Postando no Twitter: {message}")

#3. Desenvolvimento dos Adapters
class EmailAdapter(NotificationInterface):
    def __init__(self, email_service):
        self.email_service = email_service

    def send(self, message):
        """Adapta a interface da NotificationInterface para a interface do EmailService."""
        subject = "Você tem uma nova notificação"
        self.email_service.send_email(subject, message)

class SMSAdapter(NotificationInterface):
    def __init__(self, sms_service):
        self.sms_service = sms_service

    def send(self, message):
        phone_number = "1234567890"  # Número fictício para demonstração
        self.sms_service.send_sms(phone_number, message)

class TwitterAdapter(NotificationInterface):
    def __init__(self, twitter_service):
        self.twitter_service = twitter_service

    def send(self, message):
        self.twitter_service.post_tweet(message)

# Integração e Testes
if __name__ == "__main__":
    # Instâncias dos serviços
    email_service = EmailService()
    sms_service = SMSService()
    twitter_service = TwitterService()

    # Instâncias dos adapters
    email_adapter = EmailAdapter(email_service)
    sms_adapter = SMSAdapter(sms_service)
    twitter_adapter = TwitterAdapter(twitter_service)

    # Testes de envio de notificações
    email_adapter.send("Olá! Esta é uma notificação de teste por e-mail.")
    sms_adapter.send("Bem-vindo ao nosso serviço via SMS!")
    twitter_adapter.send("Olá, Twitter! Adaptando interfaces.")

