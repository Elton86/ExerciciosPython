"""Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio."""

maior_aci = total_vei = media_menor2 = cont_menor2 = total_reg = 0
menor_aci = 1000000000
lista = []

while True:
    cod = int(input("Digite o ID da cidade: "))
    if cod == 0:
        break
    else:
        num_vei = int(input("Digite o número de veiculos: "))
        total_vei += num_vei
        total_reg += 1

        num_acid = int(input("Digite o número de acidentes: "))
        lista.append((cod, num_vei, num_acid))

        if num_acid > maior_aci:
            maior_aci = num_acid
        if num_acid < menor_aci:
            menor_aci = num_acid
        if num_vei < 2000:
            media_menor2 += num_acid
            cont_menor2 += 1

print("\t\t id  vei  acid")
print(" Maior \t {}".format(*[x for x in lista if x[2] == maior_aci]))
print(" Menor \t {}".format(*[x for x in lista if x[2] == menor_aci]))
print("Media de veiculos: {:.2f}".format(total_vei / total_reg))
print("Media de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: "
      "{}".format(media_menor2 / cont_menor2))
