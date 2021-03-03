# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input("Digite o numero: "))
if num > 0:
    print("Numero {} e positivo.".format(num))
elif num < 0:
    print("Numero {} e negativo.".format(num))
else:
    print("Numero {} e neutro.".format(num))
