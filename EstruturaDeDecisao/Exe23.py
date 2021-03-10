"""Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento."""

numero = input("Digite o numero: ")

if not numero.isdecimal():
    print("{} e um numero decimal")
else:
    print("{} e um numero inteiro".format(numero))
