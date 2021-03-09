"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido."""

while True:
    nota = float(input("Digite a nota: "))
    if nota in range(0, 11):
        break
    else:
        print("Nota invalida! (Digite uma nota entre 0 e 10)")

print("Nota {} Digitada corretamente!".format(nota))
