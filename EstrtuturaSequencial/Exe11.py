"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo."""

num1 = int(input("Digite o pimeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))
num3 = float(input("Digite o numero real: "))

print("produto do dobro do primeiro com metade do segundo -> {}".format((2 * num1) * (num2 / 2)))
print("a soma do triplo do primeiro com o terceiro -> {}".format((3 * num1) + num3))
print("o terceiro elevado ao cubo -> {}".format(num3 ** 3))
