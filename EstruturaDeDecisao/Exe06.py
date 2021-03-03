# Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

maior = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print("Maior -> {}".format(maior))
