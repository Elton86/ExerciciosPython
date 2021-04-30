"""Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário."""

primos = []

num = int(input("Digite um numero inteiro: "))
divisoes = 0
for i in range(2, num + 1):
    cont = 0
    for j in range(1, num + 1):
        if i % j == 0:
            cont += 1
    if cont == 2:
        primos.append(i)

print("Numeros primos -> {}".format(primos))
