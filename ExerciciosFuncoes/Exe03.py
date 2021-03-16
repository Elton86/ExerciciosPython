"""Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos."""


def soma(a, b, c):
    print("{} + {} + {} = {}".format(a, b, c, a + b + c))


num1 = float(input("Digite o numero 1 :"))
num2 = float(input("Digite o numero 2 :"))
num3 = float(input("Digite o numero 3 :"))

soma(num1, num2, num3)
