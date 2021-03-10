"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

cont = 0
pergunta1 = input("Telefonou para a vítima? [s/n]: ")
if pergunta1.upper() == "S":
    cont += 1
pergunta1 = input("Esteve no local do crime? [s/n]: ")
if pergunta1.upper() == "S":
    cont += 1
pergunta1 = input("Mora perto da vítima? [s/n]: ")
if pergunta1.upper() == "S":
    cont += 1
pergunta1 = input("Devia para a vítima? [s/n]: ")
if pergunta1.upper() == "S":
    cont += 1
pergunta1 = input("Já trabalhou com a vítima? [s/n]: ")
if pergunta1.upper() == "S":
    cont += 1

if cont == 2:
    print("Suspeita!")
elif 2 < cont <= 4:
    print("Cúmplice!")
elif cont == 5:
    print("Assasino!")
else:
    print("Inocente!")
