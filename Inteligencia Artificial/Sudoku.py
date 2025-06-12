import random # gerar números aleatórios
import math # funções matemáticas avançadas
import copy # copiar objetos

# parametros para montar o tabuleiro
N = 9 # tamanho do tabuleiro 9x9
SUBGRIDE = 3 # tamanho de cada subgride 3x3

# montar o tabuleiro
def imprimir(tabuleiro):
    for i in range(N): # percorrer cada linha
        linha = ""
        for j in range(N): # percorrer cada coluna
            linha += str(tabuleiro[i][j]) + " " # converte o valor da célula em string e concate com " "
            if (j + 1) % 3 == 0 and j < N - 1: # a cada 3 colunas adiciona o separador de subgrade
                linha += "| "
        print(linha)
        if (i + 1) % 3 == 0 and i < N - 1: # a cada 3 linhas adiciona o separador de subgrade
            print("-" * 21)
    print('\n')


# calcula a quantidade total de conflitos (linhas e colunas)
def avaliar(tabuleiro):
    conflitos = 0
    for i in range(N):
        # Conflitos na linha i
        conflitos += N - len(set(tabuleiro[i])) # 9 - total de números únicos na linha
        # Conflitos na coluna i
        coluna = [tabuleiro[j][i] for j in range(N)]
        conflitos += N - len(set(coluna)) # 9 - total de números únicos na coluna
    return conflitos

# preenche as subgrades 3x3 nos espaços vazios
def preencher(tabuleiro_inicial):
    tabuleiro = copy.deepcopy(tabuleiro_inicial) # copia o tabuleiro
    for i in range(0, N, SUBGRIDE): # percorre a linha da subgrade
        for j in range(0, N, SUBGRIDE): # percorre a coluna da subgrade
            numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # remove os números fixos da subgrade
            for x in range(i, i + SUBGRIDE):
                for y in range(j, j + SUBGRIDE):
                    if tabuleiro[x][y] != 0: # verifica se o número é diferente de 0
                        numeros.remove(tabuleiro[x][y]) # remove o número da lista, garantindo que não haja duplicatas na subgrade

            # preenche os espaços vazios da subgrade com números aleatórios
            for x in range(i, i + SUBGRIDE):
                for y in range(j, j + SUBGRIDE):
                    if tabuleiro[x][y] == 0: # pega as posições vazias
                        # escolhe um número aleatorio da lista restante e remove o número escolhido, para evitar repetições
                        tabuleiro[x][y] = numeros.pop(random.randint(0, len(numeros) - 1))
    return tabuleiro

# esquema de vizinhos da tempera simulada
# gera um novo tabuleiro, trocando dois números na mesma subgrade 3x3
def vizinho(tabuleiro, fixos):
    novo = copy.deepcopy(tabuleiro) # gera uma cópia do tabuleiro atual

    # escolhe uma subgrade aleatória
    i = random.randint(0, SUBGRIDE - 1)
    j = random.randint(0, SUBGRIDE - 1)
    linha = i * SUBGRIDE
    coluna = j * SUBGRIDE

    # lista posições livres (não fixas) na subgrade escolhida
    livres = [
        (x, y) for x in range(linha, linha + SUBGRIDE)
        for y in range(coluna, coluna + SUBGRIDE)
        if not fixos[x][y]
    ]

    # se houver pelo menos dois valores livres, faz a troca
    if len(livres) >= 2:
        a, b = random.sample(livres, 2)
        novo[a[0]][a[1]], novo[b[0]][b[1]] = novo[b[0]][b[1]], novo[a[0]][a[1]]
    return novo


# resolve o sudoku com tempera simulada
def simulated_annealing(tabuleiro_inicial, max_iter=100000, temp_inicial=1.0, resfriamento=0.999):
    # identifica os valores fixos do tabuleiro True ou False
    fixos = [
        [tabuleiro_inicial[i][j] != 0 for j in range(N)]
        for i in range(N)
    ]

    atual = preencher(tabuleiro_inicial) # preenche o tabuleiro (cada subgrade 3x3)
    custo_atual = avaliar(atual) # quantidade de conflitos total
    temperatura = temp_inicial

    for iteracao in range(max_iter): # loop principal da tempera simulada
        if custo_atual == 0: # o problema é resolvido quando o custo é 0
            print(f"Solução encontrada em {iteracao} iterações.\n")
            return atual

        # gera uma nova solução vizinha
        novo = vizinho(atual, fixos)
        custo_novo = avaliar(novo)

        delta = custo_novo - custo_atual # calcula a diferença de custo, indica se a nova solução é melhor ou pior

        # decide se aceita a nova solução
        # se a solução for melhor (delta < 0) aceita
        # se for pior, aceita com uma probabilidade que depende de delta e a temperatura atual - evitar ficar preso em mínimos locais
        if delta < 0 or random.random() < math.exp(-delta / temperatura):
            atual, custo_atual = novo, custo_novo

        # resfria a temperatura
        temperatura *= resfriamento

    print("Limite de iterações atingido. Melhor solução aproximada:\n")
    return atual


# tabuleiro inicial do sudoku - 0 é posições vazias
entrada = [
    [0, 2, 4, 0, 0, 7, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 8, 0, 4, 1, 5],
    [4, 3, 1, 0, 0, 5, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 3, 2],
    [7, 9, 0, 0, 0, 0, 0, 6, 0],
    [2, 0, 9, 7, 1, 0, 8, 0, 0],
    [0, 4, 0, 0, 9, 3, 0, 0, 0],
    [3, 1, 0, 0, 0, 4, 7, 5, 0]
]

print("Tabuleiro de sudoku inicial:\n")
imprimir(entrada)

resultado = simulated_annealing(entrada)

print("Sudoku resolvido:\n")
imprimir(resultado)