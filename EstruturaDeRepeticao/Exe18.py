"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""

numeros = []
soma = 0

while True:
    num = int(input("Digite o numero / [-1 para sair:] "))
    if num == -1:
        break
    else:
        numeros.append(num)

maior = menor = numeros[0]

if len(numeros) == 0:
    print("Lista vazia!")
else:
    for i in numeros:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
        soma += i

print("Maior: {}".format(maior))
print("Menor: {}".format(menor))
