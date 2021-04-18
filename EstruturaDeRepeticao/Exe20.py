"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
fatorial a números inteiros positivos e menores que 16."""

while True:
    num = int(input("Digite o numero[-1 p/ sair]: "))
    if num == -1:
        print("Obrigado!")
        break
    elif num == 0:
        print('0! = 1')
    elif 1 > num or num >= 16:
        print("Digite um número entre 1 e 16!")
        continue
    else:
        fat = 1
        for i in range(1, num + 1):
            fat = fat * i
        print("{}! = {}".format(num, fat))
