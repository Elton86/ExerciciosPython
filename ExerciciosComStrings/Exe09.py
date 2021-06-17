"""Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
"""

cpf = input("Digite o cpf: ")
if ((cpf[3] or cpf[7]) != ".") \
        or (cpf[11] != "-") \
        or (not (cpf[:3] or cpf[4:8] or cpf[8:11] or cpf[12:14]).isnumeric()):
    print("CPF invalido!")
else:
    print("CPF = {}".format(cpf))
