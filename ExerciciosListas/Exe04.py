"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes."""

lista = []
consoantes = []

for i in range(10):
    lista.append(input("Digite a letra: "))
    if lista[i].upper() not in ("A", "E", "I", "O", "U"):
        consoantes.append(lista[i])
print("Consoantes: {}. Total: {}".format(consoantes, len(consoantes)))
