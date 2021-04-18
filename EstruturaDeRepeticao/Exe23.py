"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""

primos = []

num = int(input("Digite um numero inteiro: "))
divisoes = 0
for i in range(2, num + 1):
    cont = 0
    for j in range(1, num + 1):
        divisoes += 1
        if i % j == 0:
            cont += 1
    if cont == 2:
        primos.append(i)

print("Numeros primos -> {}".format(primos))
print("Total de divisões -> {}".format(divisoes))
