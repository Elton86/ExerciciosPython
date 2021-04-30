"""Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
alto e o número do aluno mais baixo, junto com suas alturas."""

alunos = {}

for i in range(5):
    cod = input("Digite o código: ")
    alunos[cod] = float(input("Digite a altura: "))

maior = 0
menor = 300

for k, v in alunos.items():
    if v > maior:
        maior = v
    if v < menor:
        menor = v

# print(maior, menor)

for k, v in alunos.items():
    if v == maior:
        print("Maior: ")
        print("ID ALluno: {} - Altura: {}".format(k, v))
    if v == menor:
        print("Menor: ")
        print("ID ALluno: {} - Altura: {}".format(k, v))
