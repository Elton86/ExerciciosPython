"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 1. salário bruto. 2.quanto pagou ao INSS. 4. quanto
pagou ao sindicato. 5. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
Obs.: Salário Bruto - Descontos = Salário Líquido."""

valorHora = float(input("Digite o valor da hora: "))
horasTrabalhadas = float(input("Digite o total de horas trabalhadas: "))

salarioBruto = valorHora * horasTrabalhadas
impostoRenda = salarioBruto * .11
inss = salarioBruto * .08
sindicato = salarioBruto * .05
desconto = impostoRenda + inss + sindicato
salarioLiquido = salarioBruto - desconto

print("Salario bruto -> {}".format(salarioBruto))
print("IR (11%) -> {}".format(impostoRenda))
print("INSS (8%) -> {}".format(inss))
print("Sindicato (5%) -> {}".format(sindicato))
print("Salario Liquido -> {}".format(salarioLiquido))
