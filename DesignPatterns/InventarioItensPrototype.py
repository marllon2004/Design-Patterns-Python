import copy

#1. Definição da Classe Protótipo de Item
class Item:
    def __init__(self, nome, categoria, efeito, valor):
        self.nome = nome
        self.categoria = categoria
        self.efeito = efeito
        self.valor = valor

    #2. Método de Clonagem
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.nome} ({self.categoria}) - Efeito: {self.efeito}, Valor: {self.valor}"

#Protótipos de Itens
pocao_prototipo = Item("Poção de Regeneração Instantanea", "Poção", "Recupera 50 pontos de vida imediatamente", 50)
arma_prototipo = Item("Espada de Zhin", "Arma", "Causa ataques flamejantes de 20 de danos", 20)
armadura_prototipo = Item("Armadura de Khan", "Armadura", "Protege contra ataques diretos em 30 pontos", 30)

#3. Personalização dos Clones
pocao_vida = pocao_prototipo.clone()
pocao_vida.nome = "Poção de Rasgo de Vida"
pocao_vida.efeito = "Recupera 30 de mana a cada ataque acertado"
pocao_vida.valor = 30

espada_fogo = arma_prototipo.clone()
espada_fogo.nome = "Espada Tiberius"
espada_fogo.efeito = "Atira sua espada causando 30 de dano"
espada_fogo.valor = 30

armadura_gelo = armadura_prototipo.clone()
armadura_gelo.nome = "Armadura Yagorath"
armadura_gelo.efeito = "Ganha defesa de 50, e resiliencia contra controle coletivo"
armadura_gelo.valor = 50

#4. Demonstração da Independência dos Clones
print("Protótipos Originais:")
print(pocao_prototipo)
print(arma_prototipo)
print(armadura_prototipo)

print("\nItens Clonados e Personalizados:")
print(pocao_vida)
print(espada_fogo)
print(armadura_gelo)

# Modificando um clone e mostrando que não afeta o protótipo original
pocao_vida.nome = "Poção de Regeneração Melhorada"
print("\nApós modificação no clone (Poção de Regeneração Melhorada):")
print(pocao_vida)
print(pocao_prototipo)  # O protótipo não foi alterado
