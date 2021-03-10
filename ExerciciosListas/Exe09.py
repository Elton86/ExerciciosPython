"""Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados
dos elementos do vetor."""

vetor = []
vetor_quad = []
soma = 0
for i in range(10):
    vetor.append(int(input("Digite o numero: ")))
    vetor_quad.append(vetor[i] ** 2)
    soma += vetor_quad[i]
print("Vetor: {}\n"
      "Quadrado do elementos: {}\n"
      "Soma: {}".format(vetor, vetor_quad, soma))
