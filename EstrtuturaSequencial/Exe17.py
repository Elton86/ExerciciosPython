"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades
de tinta a serem compradas e os respectivos preços em 3 situações: a) comprar apenas latas de 18 litros;
 b) comprar apenas galões de 3,6 litros; c) misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""
from math import ceil as arredondar

area = float(input("Digite a area de pintura: "))

litros = area / 6
latas = int(litros // 18)  # Valor sem arrendodamento.
galoes = int(litros // 3.6)  # Valor sem arrendodamento.

total_latas = total_galoes = resto_galoes_misto = 0  #
# print(latas)
if litros % 18 > 0:
    total_latas = latas + 1
    resto_galoes_misto = arredondar((litros % 18) % 3.6) #galoes adicionais apos calcular o numero de latas. (Letra C)
else:
    total_latas = latas

if litros % 3.6 > 0:
    total_galoes = galoes + 1
else:
    total_galoes = galoes

# a) comprar apenas latas de 18 litros;
print("Latas -> {}. Valor R${:.2f}".format(total_latas, total_latas * 80))

# b) comprar apenas galões de 3,6 litros;
print("Galoes -> {}. Valor R${:.2f}".format(total_galoes, total_galoes * 25))

# c) misturar latas e galões, de forma que o desperdício de tinta seja menor.
print("Latas  -> {} + Galoes -> {}. Valor R${:.2f}".format(latas, resto_galoes_misto,
                                                       latas * 80 + resto_galoes_misto * 25))
