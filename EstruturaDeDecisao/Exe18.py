"""Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."""

data = str(input("Digite a data: "))

if len(data) != 10:
    print("Data invalida!")
    exit()

data_dia = int(data[0:2])
data_mes = int(data[3:5])
data_ano = int(data[6:10])

# Depois validar corretamente de acordo com mês.
if 0 < data_dia <= 31 \
        and 0 < data_mes <= 12 \
        and 0 < data_ano \
        and len(data[6:10]) == 4 \
        and data[2] == "/" and data[5] == "/":
    print("Data digitada: {}".format(data))
else:
    print("Nao eh uma data valida!")
