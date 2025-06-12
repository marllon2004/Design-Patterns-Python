class Piece:
    """ Classe Flyweight para peças de damas. """
    def __init__(self, color, is_king=False):
        self.color = color  # Cor da peça: 'white' ou 'black'
        self.is_king = is_king  # Estado que indica se a peça é um rei

    def make_king(self):
        self.is_king = True

    def __str__(self):
        return f"{'K' if self.is_king else 'P'}-{self.color[0].upper()}"

class PieceFactory:
    """ Fábrica para criar e gerenciar peças usando Flyweight. """
    _pieces = {}

    @classmethod
    def get_piece(cls, color, is_king=False):
        key = (color, is_king)
        if key not in cls._pieces:
            cls._pieces[key] = Piece(color, is_king)
        return cls._pieces[key]

class Board:
    """ Classe para gerenciar o tabuleiro de damas. """
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        """ Inicializa o tabuleiro com peças nas posições iniciais. """
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    if i < 3:
                        self.grid[i][j] = PieceFactory.get_piece('black')
                    elif i > 4:
                        self.grid[i][j] = PieceFactory.get_piece('white')

    def draw_board(self):
        """ Desenha o tabuleiro no console. """
        for row in self.grid:
            print(' '.join(str(piece) if piece else '.' for piece in row))
        print()

class Game:
    """ Classe para controlar o jogo de damas. """
    def __init__(self):
        self.board = Board()

    def start(self):
        """ Inicia o jogo. """
        self.board.draw_board()
        # Implementar a lógica para turnos dos jogadores, verificação de vitória, etc.

# Iniciando o jogo
game = Game()
game.start()
