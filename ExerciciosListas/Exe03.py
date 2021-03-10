"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela."""

notas = list()
media = 0
for i in range(4):
    notas.append(float(input("Digite a nota {}: ".format(i + 1))))
    media += notas[i]
media /= 4
print("Notas: {}. Media: {}".format(notas, round(media, 2)))
