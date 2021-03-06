"""Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido."""

numero = int(input("Digite um numero de 1 a 7: "))

if numero == 1:
    print("{} - Domingo.".format(numero))
elif numero == 2:
    print("{} - Segunda.".format(numero))
elif numero == 3:
    print("{} - Terca.".format(numero))
elif numero == 4:
    print("{} - Quarta.".format(numero))
elif numero == 5:
    print("{} - Quinta.".format(numero))
elif numero == 6:
    print("{} - Sexta.".format(numero))
elif numero == 7:
    print("{} - Sabado.".format(numero))
else:
    print("{} eh um numero invalido.".format(numero))
