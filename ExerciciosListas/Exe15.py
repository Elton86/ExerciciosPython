"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de
dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;"""

valor = []
soma = media = quanti = x = quanti_7 = 0

while True:
    x = int(input("Digite um valor: "))
    if x != -1:
        valor.append(x)
        soma += x
    else:
        break

media = soma / len(valor)

print("Total de Elementos: {}\n"
      "Valores em ordem: {}".format(len(valor), valor))

print("Soma: {}\n"
      "Media: {}".format(soma, media))

print("Ordem inversa")
cont = len(valor)
while cont != 0:
    print(valor[cont - 1])
    cont -= 1

print("valores acima da media: ")
for i in range(len(valor)):
    if valor[i] > media:
        print(valor[i])
        quanti += 1
print("Valores acima da media: {}".format(quanti))

print("valores menores que 7: ")
for i in range(len(valor)):
    if valor[i] < 7:
        print(valor[i])
        quanti_7 += 1
print("Valores menores que 7: {}".format(quanti_7))
