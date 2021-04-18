"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""

numero_turmas = int(input("Digite o numero de turnas: "))
total_alunos = soma = media = 0

for i in range(numero_turmas):
    while True:
        total_alunos = int(input("Digite o numeros de alunos da turma {}: ".format(i + 1)))
        if total_alunos >= 40:
            print("Não pode exceder o numero de 40 alunos por turma:")
            continue
        else:
            break
    soma += total_alunos
media = soma / numero_turmas
print("Media de alunos por turma eh de {}".format(media))
