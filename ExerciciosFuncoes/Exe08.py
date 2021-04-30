"""Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado."""


def tamaho_numero(numero):
    return len(str(numero))


numero = input("Digite o numero: ")
print(tamaho_numero(numero))
