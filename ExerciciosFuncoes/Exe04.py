"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu
argumento for positivo, e ‘N’, se seu argumento for zero ou negativo."""


def func(args):
    if args > 0:
        return "P"
    return "N"


num = int(input("Digite o múmero: "))
print(func(num))
