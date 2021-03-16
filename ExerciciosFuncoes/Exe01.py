"""Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
    para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha."""


def imprimir(n):
    for j in range(n + 1):
        print(" {}".format(j) * j)


imprimir(int(input("Digite o numero: ")))
