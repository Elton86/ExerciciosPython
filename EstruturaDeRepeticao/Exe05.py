"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação."""

# Se o crescimento e de 5%, coloque 1.05.

anos = 0
populacao_A = float(input("Digite a população A: "))
crescimento_A = float(input("Digite a taxa de crescimento de A: "))
populacao_B = float(input("Digite a população A: "))
crescimento_B = float(input("Digite a taxa de crescimento de B: "))

while populacao_A < populacao_B:
    populacao_A *= crescimento_A
    populacao_B *= crescimento_B
    anos += 1

print("A ultrapassa B em {} anos.".format(anos))
