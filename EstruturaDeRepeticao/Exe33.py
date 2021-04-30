"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média
 das temperaturas."""

temperaturas = []
soma = media = 0
while True:
    temp = float(input("Digite a temperatura [0 para sair]: "))
    if temp == 0:
        break
    else:
        temperaturas.append(temp)
        soma += temp
print("Temperatura media: {}".format(soma/len(temperaturas)))
print("Temperatura maxima: {}".format(max(temperaturas)))
print("Temperatura minima: {}".format(min(temperaturas)))
