"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120"""

fat = 1
numero = ""
num = int(input("Digite o numero: "))

for i in range(1, num + 1):
    fat *= i
    numero = numero + str(i) + " . "

print("{}!".format(num), end=" = ")
print(numero[:-3], end=" = ")
print(fat)

