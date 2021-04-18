"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
votar e ao final mostrar o número de votos de cada candidato."""

total_eleitores = int(input("Digite o total de eleitores: "))
cand1 = cand2 = cand3 = 0

for i in range(total_eleitores):
    print("1 - Candidato 1: ")
    print("2 - Candidato 2: ")
    print("3 - Candidato 3: ")
    voto = int(input("Digite seu voto: "))
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1

print("* " * 5, "VOTOS", "* " * 5)
print("Candidato 1: {}".format(cand1))
print("Candidato 2: {}".format(cand2))
print("Candidato 3: {}".format(cand3))
