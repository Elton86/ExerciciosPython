"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

valor = int(input("Digite o valor: "))
resultado = ""

if 0 < valor <= 1000:
    centenas = valor // 100
    resto = valor % 100
    if centenas > 1:
        resultado += "{} Centenas. ".format(centenas)
    elif centenas == 1:
        resultado += "{} Centena. ".format(centenas)

    dezenas = resto // 10
    resto = resto % 10
    if dezenas > 1:
        resultado += "{} Dezenas. ".format(dezenas)
    elif dezenas == 1:
        resultado += "{} Dezena. ".format(dezenas)

    unidades = resto
    if unidades > 1:
        resultado += "{} Unidades. ".format(unidades)
    elif unidades == 1:
        resultado += "{} Unidade. ".format(unidades)
else:
    print("Valor invalido. Digite um numero entre 0 e 1000.")

print("Resultado: {}".format(resultado))
