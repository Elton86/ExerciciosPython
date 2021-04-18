"""Faça um programa que calcule o mostre a média aritmética de N notas."""

soma = cont = 0

while True:
    nota = float(input("Digite a nota: [-1 para sair] "))
    if nota == -1:
        break
    else:
        soma += nota
        cont += 1
print("Media = {}".format(soma / cont))
