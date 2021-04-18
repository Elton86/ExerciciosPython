"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo."""

numero = int(input("Que termo deseja encontrar: "))
ultimo = penultimo = 1

if (numero == 1) or (numero == 2):
    print("1")
else:
    for count in range(2, numero):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)
