from __future__ import annotations
import random

class Arma:
    def __init__(self, nome: str, dano_extra: int):
        self.nome = nome
        self.dano_extra = dano_extra

    def __str__(self):
        return f"{self.nome} (+{self.dano_extra} dano extra)"


class Personagem:
    def __init__(self, nome: str, classe: str, vida: int, ataque_min: int, ataque_max: int, defesa: int,
                 arma: Arma = None):
        self.nome = nome
        self.classe = classe
        self._vida = vida
        self._ataque_min = ataque_min
        self._ataque_max = ataque_max
        self._defesa = defesa
        self.arma = arma

    def get_vida(self) -> int:
        return self._vida

    def get_ataque_min(self) -> int:
        return self._ataque_min

    def get_ataque_max(self) -> int:
        return self._ataque_max

    def get_defesa(self) -> int:
        return self._defesa

    def set_vida(self, vida: int):
        if vida >= 0:
            self._vida = vida
        else:
            print("Valor de vida inválido.")

    def set_ataque_min(self, ataque_min: int):
        if ataque_min >= 0:
            self._ataque_min = ataque_min
        else:
            print("Valor de ataque mínimo inválido.")

    def set_ataque_max(self, ataque_max: int):
        if ataque_max >= self._ataque_min:
            self._ataque_max = ataque_max
        else:
            print("Valor de ataque máximo inválido.")

    def set_defesa(self, defesa: int):
        if defesa >= 0:
            self._defesa = defesa
        else:
            print("Valor de defesa inválido.")

    def __str__(self):
        return f"{self.nome}, {self.classe}, {self.get_vida()} HP, {self.get_ataque_min()} min dmg, {self.get_ataque_max()} max dmg"

    def atacar(self, personagem: Personagem) -> str:
        dano = random.randint(self.get_ataque_min(), self.get_ataque_max())

        if self.arma:
            dano += self.arma.dano_extra

        if not isinstance(personagem, Mago):
            dano = max(0, dano - personagem.get_defesa())

        if personagem.esta_vivo():
            if((personagem.get_vida() - dano) < 0):
                personagem.set_vida(0)
            else:
                personagem.set_vida(personagem.get_vida() - dano)
                return f"{self.nome} causou {dano} de dano no {personagem.nome}"

        return f"{personagem.nome} já está morto"

    def esta_vivo(self) -> bool:
        return self.get_vida() > 0

    def equipar_arma(self, arma: Arma):
        self.arma = arma

    def usar_ataque_especial(self, personagem: Personagem) -> str:
        if random.random() < 0.2 and hasattr(self, "ataque_especial"):
            return self.ataque_especial(personagem)
        else:
            return self.atacar(personagem)


class Guerreiro(Personagem):
    def ataque_especial(self, personagem: Personagem) -> str:
        dano = random.randint(self.get_ataque_min(), self.get_ataque_max())
        dano_aumentado = dano + (dano * 30 / 100)

        if personagem.esta_vivo():
            personagem.set_vida(personagem.get_vida() - dano_aumentado)
            return f"{self.nome} usou o ataque especial 'Golpe Poderoso (+30% de dano)', causando {dano_aumentado:.2f} de dano no {personagem.nome}"

        return f"{personagem.nome} já está morto"


class Mago(Personagem):
    def ataque_especial(self, personagem: Personagem) -> str:
        dano = random.randint(self.get_ataque_min(), self.get_ataque_max())

        if personagem.esta_vivo():
            personagem.set_vida(personagem.get_vida() - dano)
            return f"{self.nome} usou o ataque especial 'Bola de Fogo (ignora defesa)', causando {dano} de dano no {personagem.nome}"

        return f"{personagem.nome} já está morto"


class Arqueiro(Personagem):
    def ataque_especial(self, personagem: Personagem) -> str:
        dano = random.randint(self.get_ataque_min(), self.get_ataque_max()) * 2

        if personagem.esta_vivo():
            personagem.set_vida(personagem.get_vida() - dano)
            return f"{self.nome} usou o ataque especial 'Flecha Dupla (dois ataques menores)', causando {dano} de dano no {personagem.nome}"

        return f"{personagem.nome} já está morto"


def batalhar(personagem1: Personagem, personagem2: Personagem):
    print(f"Iniciando batalha entre {personagem1.nome} e {personagem2.nome}!\n")

    while personagem1.esta_vivo() and personagem2.esta_vivo():
        print(personagem1.usar_ataque_especial(personagem2))

        if not personagem2.esta_vivo():
            print(f"{personagem2.nome} foi derrotado!\n")
            break

        print(personagem2.usar_ataque_especial(personagem1))
        print(personagem1)

        if not personagem1.esta_vivo():
            print(f"{personagem1.nome} foi derrotado!\n")
            break

        print("-" * 50)

espada = Arma("Espada", 10)
agulha = Arma("Agulha Envenenada", 8)
arco = Arma("Arco de Caça", 6)

guerreiro = Guerreiro("Zhin", "Guerreiro", 120, 10, 20, 5, espada)
mago = Mago("Seris", "Mago", 125, 8, 18, 3, agulha)
arqueiro = Arqueiro("Shalin", "Arqueiro", 90, 6, 15, 4, arco)

mago.equipar_arma(agulha)
arqueiro.equipar_arma(arco)

batalhar(guerreiro, mago)
