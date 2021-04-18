"""Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas."""


def somaImposto(txImpos, custo):
    return txImpos * custo / 100 + custo


taxa = float(input("Digite a taxa (ex: 30%): "))
custo_taxa = float(input("Digite o custo: "))
print("Valor final: {}".format(somaImposto(taxa, custo_taxa)))
