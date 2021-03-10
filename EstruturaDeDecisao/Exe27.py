"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de
maças adquiridas e escreva o valor a ser pago pelo cliente."""

maca = float(input("Quantos kg de maçã? "))
morango = float(input("Quantos kg de morango? "))
preco_morango = preco_maca = desconto = 0
total_kg = maca + morango

if morango > 5:
    preco_morango = morango * 2.2
else:
    preco_morango = morango * 2.5

if maca > 5:
    preco_maca = maca * 1.5
else:
    preco_maca = maca * 1.8

preco_total = preco_maca + preco_morango

if total_kg > 8 or preco_total > 25:
    desconto = preco_total * .1

print("Morango {}kg - Preço R${:.2f}\n"
      "Maca {}kg - Preço R${:.2f}\n"
      "Peso Total {}kg\n"
      "Subtotal R${:.2f}\n"
      "Desconto: R${:.2f}\n"
      "Preco Final R${:.2f}".format(morango, preco_morango, maca,
                                    preco_maca, total_kg, preco_total,
                                    desconto, preco_total - desconto))
