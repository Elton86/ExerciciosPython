"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
quatro notas de 10, uma nota de 5 e quatro notas de 1."""

valor = int(input("Digite o valor do saque: "))
resto = 0
if 10 < valor <= 600:
    notas_cem = valor // 100
    resto = valor % 100
    notas_cinquenta = resto // 50
    resto %= 50
    notas_dez = resto // 10
    resto %= 10
    notas_cinco = resto // 5
    resto %= 5
    notas_um = resto

    print("Notas de 100: {:3d}\n"
          "Notas de 50: {:4d}\n"
          "Notas de 10: {:4d}\n"
          "Notas de 5: {:5d}\n"
          "Notas de 1: {:5d}\n".format(notas_cem, notas_cinquenta, notas_dez, notas_cinco, notas_um))
else:
    print("Valor mínimo =  R$10. Valor Máximo R$600. Recomece.")
