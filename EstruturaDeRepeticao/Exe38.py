"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que
o usuário digite o salário inicial do funcionário."""

salario = 1000
ano_atual = 2021
ano_entrada = int((input("Digite o ano de entrada: ")))
reajuste = 0.015

for i in range(ano_entrada, ano_atual + 1):
    print("Ano: ", i)
    print("Salario anterior: R$", round(salario, 2))
    salario *= 1 + reajuste
    print("Salario reajustado: R$", round(salario, 2))
    print("Reajuste: {:.2%}".format(reajuste))
    reajuste *= 2
    print()



