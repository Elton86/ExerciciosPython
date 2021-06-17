"""Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o
 nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973."""


def valida_data(date):
    if len(date) != 10:
        return False
    else:
        dia = int(date[:2])
        mes = int(date[3:5])
        ano = int(date[6:10])
        if (dia > 29 and mes == 2) \
                or (dia < 1 or dia > 31) \
                or (mes > 12 or mes < 1) \
                or (ano > 2021 or ano < 0) \
                or (date[2] and date[5]) != "/":
            return False
        else:
            return True


def data_exten(date):
    mes_ext = ""
    mes = int(date[3:5])
    if mes == 1:
        mes_ext = "Jan"
    elif mes == 2:
        mes_ext = "Fev"
    elif mes == 3:
        mes_ext = "Mar"
    elif mes == 4:
        mes_ext = "Abr"
    elif mes == 5:
        mes_ext = "Mai"
    elif mes == 6:
        mes_ext = "Jun"
    elif mes == 7:
        mes_ext = "Jul"
    elif mes == 8:
        mes_ext = "Ago"
    elif mes == 9:
        mes_ext = "Set"
    elif mes == 10:
        mes_ext = "Out"
    elif mes == 11:
        mes_ext = "Nov"
    elif mes == 12:
        mes_ext = "Dez"

    return "{} de {} de {}".format(date[:2], mes_ext, date[6:10])


while True:
    data = input("Digite a data: ")
    if valida_data(data):
        print(data_exten(data))
    else:
        print("Data invalida!")
