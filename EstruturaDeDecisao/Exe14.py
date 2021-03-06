"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."""

nota1 = float(input("Digite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))
media = (nota1 + nota2) / 2

if 10 >= media >= 9:
    print("Nota 1->{:4}, Nota 2->{:4} ---- Media->{:4}, Aluno APROVADO com conceito A".format(nota1, nota2, media))
elif 9 > media >= 7.5:
    print("Nota 1->{:4}, Nota 2->{:4} ---- Media->{:4}, Aluno APROVADO com conceito B".format(nota1, nota2, media))
elif 7.5 > media >= 6:
    print("Nota 1->{:4}, Nota 2->{:4} ---- Media->{:4}, Aluno APROVADO com conceito C".format(nota1, nota2, media))
elif 6 > media >= 4:
    print("Nota 1->{:4}, Nota 2->{:4} ---- Media->{:4}, Aluno REPROVADO com conceito D".format(nota1, nota2, media))
elif 4 > media >= 0:
    print("Nota 1->{:4}, Nota 2->{:4} ---- Media->{:4}, Aluno REPROVADO com conceito E".format(nota1, nota2, media))
else:
    print("NOTAS INVALIDAS!")
