"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""

numeros = []
soma = 0

while True:
    num = int(input("Digite o numero / [-1 para sair:] "))
    if num == -1:
        break
    elif 0 > num or num > 1000:
        print("Digite um numero entre 0 e 1000!!")
        continue
    else:
        numeros.append(num)

maior = menor = numeros[0]

if len(numeros) == 0:
    print("Lista vazia!")
else:
    for i in numeros:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
        soma += i

print("Maior: {}".format(maior))
print("Menor: {}".format(menor))

