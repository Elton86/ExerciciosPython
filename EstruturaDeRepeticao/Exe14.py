"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
números impares."""
par = impar = 0
for i in range(10):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print("Total de pares: {}".format(par))
print("Total de impares: {}".format(impar))
