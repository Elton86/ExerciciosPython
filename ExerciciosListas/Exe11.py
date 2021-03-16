"""Altere o programa anterior, intercalando 3 vetores de 10 elementos cada."""

vetor_intercalado = []
vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    vetor1.append(input("Digite o elemento para o vetor 1: "))
for i in range(10):
    vetor2.append(input("Digite o elemento para o vetor 2: "))
for i in range(10):
    vetor3.append(input("Digite o elemento para o vetor 3: "))
for i in range(10):
    vetor_intercalado.append(vetor1[i])
    vetor_intercalado.append(vetor2[i])
    vetor_intercalado.append(vetor3[i])

print("Vetor_1: {}\n"
      "Vetor_2: {}\n"
      "Vetor_3: {}\n"
      "Vetor_Final: {}".format(vetor1, vetor2, vetor3, vetor_intercalado))
