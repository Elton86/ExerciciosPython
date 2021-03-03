"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato."""

valor1 = float(input("Digite o primeiro preco: "))
valor2 = float(input("Digite o segundo preco: "))
valor3 = float(input("Digite o terceiro preco: "))

menor = valor1

if valor2 < menor:
    menor = valor2
if valor3 < menor:
    menor = valor3

print("Produto com menor preco-> R${}".format(menor))
