# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

hora = float(input("Quantas horas vc trabalhou?"))
valor_hora = float(input("Qual o valor da hora?"))
print("Salario a receber: {}".format(hora * valor_hora))
