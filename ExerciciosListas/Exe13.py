"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule
a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."""

mes = []
media = 0

for i in range(12):
    mes_nome = str(input("Digite o mes: "))
    temp = float(input("Digite a temperatura: "))
    mes.append([mes_nome, temp])
    media += temp
media /= 12

for i in range(12):
    if mes[i][1] > media:
        print("Mes {} - Media {}".format(mes[i][0], mes[i][1]))
