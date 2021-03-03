# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

maior = num1
meio = num1
menor = num1

if num1 < num2 > num3:
    maior = num2
if num1 < num3 > num2:
    maior = num3

if num1 > num2 < num3:
    menor = num2
if num1 > num3 < num2:
    menor = num3

if num1 < num2 < num3 or num3 < num2 < num1:
    meio = num2
if num1 > num3 > num2 or num1 < num3 < num2:
    meio = num3
if num3 > num1 > num2 or num3 < num1 < num2:
    meio = num1

print("Ordem descrecente -> {}, {} e {}".format(maior, meio, menor))
