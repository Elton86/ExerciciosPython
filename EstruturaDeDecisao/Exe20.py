"""Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10."""

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print("Aprovado com Distinção com media {}".format(media))
elif media >= 7:
    print("Aprovado com media {}".format(media))
else:
    print("Reprovado com media {}".format(media))
