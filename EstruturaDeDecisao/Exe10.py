"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

turno = str(input("Digite o turno: "))

if turno in ("m", "M"):
    print("Bom dia!")
elif turno in ("t", "T"):
    print("Boa tarde!")
elif turno in ("n", "N"):
    print("Boa noite!")
else:
    print("Valor inválido!")
