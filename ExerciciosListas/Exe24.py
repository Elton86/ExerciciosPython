"""Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar
numeros aleatórios, simulando os lançamentos dos dados."""

from random import randrange

dados = []
um = dois = tres = quatro = cinco = seis = 0

for i in range(100):
    resultado = randrange(1, 7)
    dados.append(resultado)
    if resultado == 1:
        um += 1
    elif resultado == 2:
        dois += 1
    elif resultado == 3:
        tres += 1
    elif resultado == 4:
        quatro += 1
    elif resultado == 5:
        cinco += 1
    else:
        seis += 1

print("1: {}\n"
      "2: {}\n"
      "3: {}\n"
      "4: {}\n"
      "5: {}\n"
      "6: {}\n".format(um, dois, tres, quatro, cinco, seis))
