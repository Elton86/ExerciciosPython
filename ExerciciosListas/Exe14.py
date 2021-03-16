"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente"."""

lista = []
soma = 0
lista.append(input("Telefonou para a vítima? [s/n]: "))
lista.append(input("Esteve no local do crime? [s/n]: "))
lista.append(input("Mora perto da vítima? [s/n]: "))
lista.append(input("Devia para a vítima? [s/n]: "))
lista.append(input("Já trabalhou com a vítima? [s/n]: "))

for i in range(5):
    if lista[i].upper() == "S":
        soma += 1

print(soma)
if soma == 2:
    print("Suspeita")
elif soma == 3 or soma == 4:
    print("Cúmplice")
elif soma == 5:
    print("Assassino")
else:
    print("Inocente")
