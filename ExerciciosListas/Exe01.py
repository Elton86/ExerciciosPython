"""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""

vetor = []
for i in range(5):
    vetor.append(int(input("Digite o numero {}: ".format(i + 1))))
print(vetor)
