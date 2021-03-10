"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""

vetor = []
for i in range(10):
    vetor.append(int(input("Digite o numero {}: ".format(i + 1))))
print("Vetor Digitado: {}".format(vetor))
print("Vetor Ordem Inversa: {}".format(vetor[::-1]))
