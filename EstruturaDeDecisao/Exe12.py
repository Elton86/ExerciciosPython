"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""

horas = float(input("Digite o total de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))
salario_bruto = horas * valor_hora

if salario_bruto <= 900:
    IR = "Isento"
    imposto_total = 0
elif 900 < salario_bruto <= 1500:
    IR = "5%"
    imposto_total = salario_bruto * .05
elif 1500 < salario_bruto <= 2500:
    IR = "10%"
    imposto_total = salario_bruto * .1
else:
    IR = "20%"
    imposto_total = salario_bruto * .2

fgts = salario_bruto * .11
inss = salario_bruto * .1
sindicato = salario_bruto * .03220
total_descontos = fgts + sindicato + inss + imposto_total
salario_liquido = salario_bruto - total_descontos

print('Salário Bruto \t\t: {:.2f}\n'
      '(-) IR ({}) \t\t: {:.2f}\n'
      'FGTS (11%) \t\t\t: {:.2f}\n'
      '(-) INSS (10%) \t\t: {:.2f}\n'
      '(-) Sindicato (3%) \t: {:.2f}\n'
      'Total de descontos \t: {:.2f}\n'
      'Salario Liquido \t: {:.2f}\n'
      .format(salario_bruto, IR, imposto_total, fgts, inss, sindicato, total_descontos, salario_liquido), end=" ")
