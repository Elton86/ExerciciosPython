"""Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u."""

frase = input("Digite a frase: ")
cont_esp = cont_vog = 0
for f in frase:
    if f == " ":
        cont_esp += 1
    elif f.lower() in ("a", "e", "i", "o", "u"):
        cont_vog += 1

print("Frase: {}".format(frase))
print("Total de espaços em branco: {}".format(cont_esp))
print("Total de vogais: {}".format(cont_vog))
