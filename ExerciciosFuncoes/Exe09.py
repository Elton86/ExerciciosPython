"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""


def inverte_num(num):
    return num[::-1]


numero = input("Digite o numero: ")
print(inverte_num(numero))
