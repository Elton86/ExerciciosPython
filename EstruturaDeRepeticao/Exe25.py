"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
média calculada."""

soma = cont = 0

while True:
    idade = int(input("Digite a idade[-1 para sair]: "))
    if idade == -1:
        break
    else:
        soma += idade
        cont += 1

media = soma / cont
print("Media = {}".format(media))

if 0 <= media <= 25:
    print("turma é jovem!")
elif 25 < media <= 60:
    print("turma é adulta!")
else:
    print("turma é idosa!")
