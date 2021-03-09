"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tamanho_arquivo = float(input("Digite o tamanho do arquivo: "))
velocidade = float(input("Digite o tamanho da velocidade: "))

taxa = velocidade / 8  # Conversao de Mb para Mb
tempo_min = round((tamanho_arquivo / taxa) / 60, 2)  # Conversao do tempo para minutos.

print("Tempo aproximado: {}min".format(tempo_min))
