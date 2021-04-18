"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""

soma = media = 0
quant_cd = int(input("Digite o número de CD's: "))

for i in range(quant_cd):
    valor_cd = float(input("Digite o vallor do CD {}: ".format(i + 1)))
    soma += valor_cd
media = soma / quant_cd

print("Valor total = R${}".format(soma))
print("Valor medio por CD = R${}".format(media))
