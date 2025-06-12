# Marllon Silva Araujo Coelho - 627021
# Interface Tema
class Tema:
    def aplicar_tema(self):
        pass

# Implementações concretas de Tema
class TemaClaro(Tema):
    def aplicar_tema(self):
        return "Aplicando tema claro."

class TemaEscuro(Tema):
    def aplicar_tema(self):
        return "Aplicando tema escuro."

class TemaContraste(Tema):
    def aplicar_tema(self):
        return "Aplicando tema de alto contraste."

# Classe base para todos os componentes de GUI
class ComponenteGUI:
    def __init__(self, tema: Tema):
        self.tema = tema  # Composição: cada componente tem um tema

    def desenhar(self):
        pass

# Componentes específicos
class Botao(ComponenteGUI):
    def desenhar(self):
        return f"Botão desenhado. {self.tema.aplicar_tema()}"

class CaixaSelecao(ComponenteGUI):
    def desenhar(self):
        return f"Caixa de Seleção desenhada. {self.tema.aplicar_tema()}"

class CaixaTexto(ComponenteGUI):
    def desenhar(self):
        return f"Caixa de Texto desenhada. {self.tema.aplicar_tema()}"

# Criação de instâncias de componentes com diferentes temas
tema_claro = TemaClaro()
tema_escuro = TemaEscuro()
tema_contraste = TemaContraste()

# Botões com diferentes temas
botao_claro = Botao(tema_claro)
botao_escuro = Botao(tema_escuro)
botao_contraste = Botao(tema_contraste)

# Caixa de Seleção com diferentes temas
caixa_selecao_claro = CaixaSelecao(tema_claro)
caixa_selecao_escuro = CaixaSelecao(tema_escuro)
caixa_selecao_contraste = CaixaSelecao(tema_contraste)

# Caixa de Texto com diferentes temas
caixa_texto_claro = CaixaTexto(tema_claro)
caixa_texto_escuro = CaixaTexto(tema_escuro)
caixa_texto_contraste = CaixaTexto(tema_contraste)

# Exemplo de execução:
print(botao_claro.desenhar())
print(botao_escuro.desenhar())
print(botao_contraste.desenhar())

print(caixa_selecao_claro.desenhar())
print(caixa_selecao_escuro.desenhar())
print(caixa_selecao_contraste.desenhar())

print(caixa_texto_claro.desenhar())
print(caixa_texto_escuro.desenhar())
print(caixa_texto_contraste.desenhar())
