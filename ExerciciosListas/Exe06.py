"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0."""
notas_medias = []

for i in range(10):
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    print("*" * 20)
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 7:
        notas_medias.append(media)

print("Total de alunos com media 7: {} - {}".format(len(notas_medias), notas_medias))
