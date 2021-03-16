"""Faça um programa que leia 5 números e informe a soma e a média dos números."""

vetor = []
soma = 0

for i in range(5):
    vetor.append(int(input("Digite o numero: ")))
    soma += vetor[i]

media = soma / 5

print("Vetor: {}\n"
      "Media: {}\n"
      "Soma: {}".format(vetor, media, soma))
