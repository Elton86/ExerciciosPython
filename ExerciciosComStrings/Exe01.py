"""Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente."""

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

print("String 1: {} - Tamanho: {}".format(string1, len(string1)))
print("String 2: {} - Tamanho: {}".format(string2, len(string2)))
if string1 == string2:
    print("Strings iguais:")
else:
    print("String diferentes")
if len(string1) == len(string2):
    print("Tamanho igual")
else:
    print("Tamanhos diferentes")

