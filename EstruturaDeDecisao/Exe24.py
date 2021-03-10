"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
- par ou ímpar;
- positivo ou negativo;
- inteiro ou decimal."""

numero = input("Digite o numero: ")

if numero.isdecimal():
    print("E um numero inteiro")
    if float(numero) % 2 == 0:  # So verifica se o numero e par/impar se for valor inteiro.
        print("Numero par")
    else:
        print("Numero impar")
else:
    print("E um numero decimal")

if float(numero) > 0:
    print("Numero positivo")
elif float(numero) < 0:
    print("Numero negativo")
else:
    print("Numero neutro")
