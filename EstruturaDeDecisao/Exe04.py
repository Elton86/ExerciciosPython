# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digte a letra: "))

if letra.lower() in ("a", "e", "i", "o", "u"):
    print("{} eh uma vogal!".format(letra))
else:
    print("{} eh uma consoante!".format(letra))
