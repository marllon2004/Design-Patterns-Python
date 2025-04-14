import copy

#1. Definir uma classe de Protótipo
class Inimigo:
    def __init__(self, tipo, nivel, pontos_vida):
        self.tipo = tipo
        self.nivel = nivel
        self.pontos_vida = pontos_vida
    #2. Implementar a clonagem
    def clone(self):
        return copy.deepcopy(self)

#Desafio. Criar três tipos diferentes de inimigos (por exemplo, Orc, Troll, e Goblin) usando apenas um protótipo e o método clone().
#Protótipo Original
orcs = Inimigo("Orc", 16, 1010)

#Protótipos Clones
troll = orcs.clone()
goblin = orcs.clone()

#3. Personalização dos clones
#Desafio. Após clonar, modifique os atributos nivel e pontos_vida para fazer cada clone único.
troll.nivel = 19
troll.pontos_vida = 845

goblin.nivel = 12
goblin.pontos_vida = 500

#4. Demonstrar Independência dos Clones
#Desafio. Imprima os atributos de cada clone para demonstrar que são independentes entre si e do protótipo
print("Protótipo Orc:")
print(f"Tipo: {orcs.tipo}, Nível: {orcs.nivel}, Pontos de Vida: {orcs.pontos_vida}\n")

print("Clone Troll:")
print(f"Tipo: {troll.tipo}, Nível: {troll.nivel}, Pontos de Vida: {troll.pontos_vida}\n")

print("Clone Goblin:")
print(f"Tipo: {goblin.tipo}, Nível: {goblin.nivel}, Pontos de Vida: {goblin.pontos_vida}\n")

# Alterando o protótipo para mostrar a independência
orcs.nivel = 1
orcs.pontos_vida = 230

print("--- Após alteração do protótipo Orc: ---")
print(f"Protótipo Orc - Nível: {orcs.nivel}, Pontos de Vida: {orcs.pontos_vida}")
print(f"Troll - Nível: {troll.nivel}, Pontos de Vida: {troll.pontos_vida}")
print(f"Goblin - Nível: {goblin.nivel}, Pontos de Vida: {goblin.pontos_vida}")
