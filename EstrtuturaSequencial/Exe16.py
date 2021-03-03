"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
e o preço total."""

area = float(input("Digite a quantidade de metros quadrados para pintura: "))
total_litros = area / 3
latas = total_litros / 18
print("Total de litros -> {:.2f}. Total de latas -> {:.2f}. Total do valor -> R${:.2f}"
      .format(total_litros, latas, latas * 80))
