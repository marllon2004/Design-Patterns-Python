#Danielle Bassetto RA: 629391
#Marllon Silva Araujo Coelho RA: 627021

import pandas as panda #biblioteca para criar a tabela

def f(x): #f(x) = x^3 + 3x - 1
    return x ** 3 + 3 * x - 1


# intervalos [a, b] -> [0,1]
a, b = 0, 1

# margem erro
E = 0.001

tabela = []
k = 0

while (b - a) >= E:
    xk = (a + b) / 2
    fa = f(a)
    fxk = f(xk)

    # determinando novo intervalo
    if fa * fxk < 0:
        b = xk
        sinal = "-"
    else:
        a = xk
        sinal = "+"

    #adicionando na tabela
    tabela.append([k, round(a, 6), round(b, 6), round(xk, 6), round(fa, 6), round(fxk, 6), sinal, (b - a < E)])
    k += 1

# adicionando as colunas da tabela
colunas = ["k", "a", "b", "xk", "f(a)", "f(xk)", "sinal", "E < 0,001"]
df = panda.DataFrame(tabela, columns=colunas)

# mostrando tabela e a raiz
print(df)
print(f"\nRaiz aproximada: {round(xk, 6)}")