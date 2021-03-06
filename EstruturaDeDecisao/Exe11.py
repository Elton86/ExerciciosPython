"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para
desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o
reajuste segundo o seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento."""

salario = float(input("Digite o seu salario: "))
reajuste = percentual = 0

if salario <= 280:
    reajuste = salario * .2
    percentual = 20
    novo_salario = salario + reajuste
elif 280 < salario <= 700:
    reajuste = salario * .15
    percentual = 15
    novo_salario = salario + reajuste
elif 700 < salario <= 1500:
    reajuste = salario * .1
    percentual = 10
    novo_salario = salario + reajuste
elif salario > 1500:
    reajuste = salario * .05
    percentual = 5
    novo_salario = salario + reajuste

print("Salario anterior -> R${:.2f},\n "
      "percentual de aumento aplicado -> {}%,\n"
      "valor do aumento -> R${:.2f},\n "
      "novo salário -> R${:.2f}"
      .format(salario, percentual, reajuste, salario + reajuste))
