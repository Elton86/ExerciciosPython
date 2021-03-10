"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar."""

desconto_cartao = valor_compra = 0

tipo_carne = str(input("Deseja qual tipo de Carne? [P - Picanha / A - Alcatra / F - File Duplo]: "))
peso_carne = float(input("Quantas Kg deseja comprar? "))
tipo_pagamento = str(input("Qual o tipo de pagamento? [C - Cartão Tabajara / D - Dinheiro]: "))

if tipo_carne.upper() == "F":
    tipo_carne = "File Duplo"
    if peso_carne > 5:
        valor_compra = peso_carne * 5.8
    else:
        valor_compra = peso_carne * 4.9

if tipo_carne.upper() == "A":
    tipo_carne = "Alcatra"
    if peso_carne > 5:
        valor_compra = peso_carne * 6.8
    else:
        valor_compra = peso_carne * 5.9

if tipo_carne.upper() == "P":
    tipo_carne = "Picanha"
    if peso_carne > 5:
        valor_compra = peso_carne * 7.8
    else:
        valor_compra = peso_carne * 6.9

if tipo_pagamento.upper() == "C":
    desconto_cartao = valor_compra * .05

print("Tipo de Carne: {}\n"
      "Peso: {}Kg\n"
      "Preço Total R${:.2f}\n"
      "Desconto-Cartao-Tabajara: R${:.2f}\n"
      "Preço Final R${:.2f}".format(tipo_carne, peso_carne, valor_compra, desconto_cartao,
                                    valor_compra - desconto_cartao))
