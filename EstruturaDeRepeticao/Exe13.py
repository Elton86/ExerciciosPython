"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao
segundo número. Não utilize a função de potência da linguagem."""

base = int(input("Digite a base: "))
epx = int(input("Digite a expoente: "))
resultado = 1

for i in range(0, epx):
    resultado *= base
print("Resultado: {}".format(resultado))
