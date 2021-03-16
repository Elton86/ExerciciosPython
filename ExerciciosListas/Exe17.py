"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco
distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o
 exemplo abaixo:
 Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m"""

atletas = []
soma = 0
nome = ""
while True:
    cont = soma = 0
    nome = str(input("Digite o nome: "))
    if nome == "":
        break
    else:
        saltos = []
        for i in range(5):
            salto = float(input("Digite a nota: "))  # Esta duplicando
            saltos.append(salto)
            soma += salto
        media = soma / 5
        atletas.append([nome, saltos, media])

for i in range(len(atletas)):
    print("Nome: {} - Notas: {} - Media: {}"
          .format(atletas[i][0], atletas[i][1], atletas[i][2]))
