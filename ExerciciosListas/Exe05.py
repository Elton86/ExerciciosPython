"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""

vetor = []
vetor_par = []
vetor_impar = []

for i in range(20):
    vetor.append(int(input("Digite a numero: ")))
    if vetor[i] % 2 == 0:
        vetor_par.append(vetor[i])
    else:
        vetor_impar.append(vetor[i])

print("Vetor: {}\nVetor Par: {}\n Vetor Impar: {}".format(vetor, vetor_par, vetor_impar))
