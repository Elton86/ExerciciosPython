# Jogo da Forca - Frutas

import random

# Gera uma fruta aleatória.
frutas = ("GRAVIOLA", "LARANJA", "AMORA", "PITANGA", "CAJU", "MANGA", "GOIABA",
          "MANGABA", "ACEROLA")
palavra_secreta = frutas[random.randrange(0, len(frutas))]
palavra_secreta_lista = []

for i in range(1, len(palavra_secreta) + 1):
    palavra_secreta_lista.append('_')

print(palavra_secreta_lista)

acerto = False
enforcado = False
erros = 0

while not acerto and not enforcado:
    letra = input('Digite a letra: ')
    if letra.upper() in palavra_secreta:
        for i in range(0, len(palavra_secreta)):
            if letra.upper() == palavra_secreta[i]:
                palavra_secreta_lista[i] = letra.upper()
    else:
        erros += 1
    print(palavra_secreta_lista)
    print('Erros = {}'.format(erros))

    acerto = '_' not in palavra_secreta_lista
    enforcado = bool(erros == 5)  # limite de 5 erros.

if acerto:
    print('Vc acertou! A palavra era {} Parabéns!!'.format(palavra_secreta))
else:
    print('Vc não conseguiu acertar!! A palavra era {}.'.format(palavra_secreta))
