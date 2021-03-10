"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida."""
idade = []
altura = []
for i in range(5):
    idade.append(int(input("Digite a idade: ")))
    altura.append(float(input("Digite a altura: ")))

print(idade[::-1])
print(altura[::-1])
