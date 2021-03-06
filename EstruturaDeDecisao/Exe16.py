"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
- Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
demais valores, sendo encerrado;
- Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
- Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
- Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""

from math import sqrt

a = float(input("Digite o valor de a: "))
b = c = 0
if a == 0:
    print(" Valor invalido. Nao eh uma equacao de 2º grau. ")
    exit()
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("A equacao no possui raizes reais.")
elif delta == 0:
    print("Delta igual a 0. Apenas uma raiz real -> {}".format(-b / (2 * a)))
else:
    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)
    print("A equacao possui duas raizes reais: {} e {}".format(x1, x2))
