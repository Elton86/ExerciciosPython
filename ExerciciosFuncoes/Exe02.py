"""Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha."""


def imprimir(n):
    for i in range(n):
        i += 1
        print("{} ".format(str(i) * i))


imprimir(int(input('Digite um número: ')))
