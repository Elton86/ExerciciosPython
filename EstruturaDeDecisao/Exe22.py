"""Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão)."""

numero = int(input("Digite um numero inteiro: "))

if numero % 2 == 0:
    print("{} e par!".format(numero))
else:
    print("{} e impar!".format(numero))
