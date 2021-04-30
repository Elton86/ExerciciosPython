"""Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro
 e determine se ele é ou não um número primo."""
cont = 0
num = int(input("Digite um numero: "))
for i in range(1, num + 1):
    print(num, i, num % i)
    if num % i == 0:
        cont += 1
if cont == 2:
    print("{} eh Primo")
else:
    print("{} nao eh Primo".format(num))
