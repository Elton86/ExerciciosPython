"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele
é divisível."""
lista_divisiveis = []

num = int(input("Digite um numero inteiro: "))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        cont += 1
        lista_divisiveis.append(i)
if cont == 2:
    print("{} é primo!".format(num))
else:
    print("{} não é primo! E é divisivel por {}".format(num, lista_divisiveis))
