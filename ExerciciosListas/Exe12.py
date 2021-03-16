"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13
anos possuem altura inferior à média de altura desses alunos."""

alunos = []
lista_nova_alunos = []
media = 0
for i in range(20):
    alunos.append([int(input("Digite a idade: ")), float(input("Digite a altura: "))])
    media += alunos[i][1]
media /= 20

for i in range(20):
    if alunos[i][1] >= media:
        lista_nova_alunos.append(alunos[i])

print("Alunos: {}".format(alunos))
print("Alunos Acima da Media: {}".format(lista_nova_alunos))
