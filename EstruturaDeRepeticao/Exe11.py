"""Altere o programa anterior para mostrar no final a soma dos números."""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
soma = 0
for i in range(num1 + 1, num2):
    print(i)
    soma += i
print("Soma {}".format(soma))
