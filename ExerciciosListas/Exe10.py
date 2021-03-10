"""Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores."""

vetor_intercalado = []
vetor1 = []
vetor2 = []

for i in range(10):
    vetor1.append(input("Digite o elemento para o vetor 1: "))
for i in range(10):
    vetor2.append(input("Digite o elemento para o vetor 2: "))
for i in range(10):
    vetor_intercalado.append(vetor1[i])
    vetor_intercalado.append(vetor2[i])

print("Vetor_1: {}\n"
      "Vetor_2: {}\n"
      "Vetor_Final: {}".format(vetor1, vetor2, vetor_intercalado))
