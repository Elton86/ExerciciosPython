"""Faça um programa que leia 5 números e informe o maior número."""

vetor = []

for i in range(5):
    vetor.append(int(input("Digite o numero: ")))
maior = vetor[0]
for i in range(5):
    if vetor[i] > maior:
        maior = vetor[i]

print("Vetor: {}\n"
      "Maior: {}".format(vetor, maior))
