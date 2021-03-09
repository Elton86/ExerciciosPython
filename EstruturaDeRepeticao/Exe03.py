"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

while True:
    nome = str(input("Digite o nome: "))
    if len(nome) < 4:
        print("Nome menor que 4 caracteres. Digite novamente.")
        continue
    break

while True:
    idade = int(input("Digite a idade: "))
    if not 0 <= idade <= 150:
        print("Digite uma idade entre 0 e 150. Digite novamente.")
        continue
    break

while True:
    salario = float(input("Digite salario: "))
    if salario <= 0:
        print("Digite um salario maior que 0. Digite novamente.")
        continue
    break

while True:
    sexo = str(input("Digite o sexo: "))
    if sexo.upper() not in ("F", "M"):
        print("Digite um sexo valido (F ou M). Digite novamente.")
        continue
    break

while True:
    estado_civil = str(input("Digite o estado civil: "))
    if estado_civil.upper() not in ("C", "S", "V", "D"):
        print("Digite um estado civil valido (C, S, V ou D). Digite novamente.")
        continue
    break

print(10 * "*" + " INFO " + 10 * "*")
print("Nome -> {}".format(nome))
print("Idade -> {}".format(idade))
print("Sexo -> {}".format(sexo))
print("Estado Civil -> {}".format(estado_civil))
