"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""

numeros = []
soma = 0
produto = 1

for i in range(5):
    numeros.append(int(input("Digite um numero inteiro:")))
    soma += numeros[i]
    produto *= numeros[i]

print("Numeros: {}. Produto: {} Soma: {}".format(numeros, produto, soma))
