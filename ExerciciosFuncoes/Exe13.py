"""Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função
deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor
máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de
forma elegante."""


# falta concluir.
def moldura(linha, coluna):
    if linha < 1 or linha > 20:
        linha = 1
    if coluna < 1 or coluna > 20:
        coluna = 1

    for i in range(linha):
        print("* " * coluna)
    print()
    for i in range(linha):
        print("- " * coluna)
    print()
    for i in range(linha):
        print("/ " * coluna)


linhas = int(input("Digite o numero de linhas: "))
colunas = int(input("Digite o numero de colunas: "))
moldura(linhas, colunas)
