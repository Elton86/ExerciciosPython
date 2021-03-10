"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo
cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""

preco_gas = 2.5
preco_alc = 1.9

litros = float(input("Digite o total de litros: "))
tipo = input("Digite o tipo do combustivel: [A]Alcool - [G]Gasolina: ")

if tipo.upper() == "G":
    if litros > 20:
        print("{} litros de Gaoslina. Valor R${:.2f}.".format(litros, litros * preco_gas * 0.94))
    else:
        print("{} litros de Gaoslina. Valor R${:.2f}.".format(litros, litros * preco_gas * 0.96))

if tipo.upper() == "A":
    if litros > 20:
        print("{} litros de Alcool. Valor R${:.2f}.".format(litros, litros * preco_alc * 0.95))
    else:
        print("{} litros de Alcool. Valor R${:.2f}.".format(litros, litros * preco_alc * 0.97))
