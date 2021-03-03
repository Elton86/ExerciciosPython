"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminino, M - Masculino, Sexo Inválido."""

letra = str(input("Digite a letra: "))
if letra in ("f", "F"):
    print("F - Feminino")
elif letra in ("M", "m"):
    print("M - Masculino")
else:
    print("Sexo invalida!")
