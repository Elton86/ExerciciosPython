"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o
mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua
altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais
gordo e do mais magro, além da média das alturas e dos pesos dos clientes"""

mais_alto = mais_gordo = media_altura = media_peso = cont = 0
mais_baixo = mais_magro = 1000
pessoa_mais_alta = pessoa_mais_baixa = pessoa_mais_magra = pessoa_mais_gorda = ()

while True:
    cod = int(input("Digite seu codigo: "))
    if cod == 0:
        break
    else:
        alt = float(input("Digite sua altura: "))
        peso = float(input("Digite seu peso: "))
        media_altura += alt
        media_peso += peso
        cont += 1
        if alt > mais_alto:
            mais_alto = alt
            pessoa_mais_alta = cod, alt, peso
        if peso > mais_gordo:
            mais_gordo = peso
            pessoa_mais_gorda = cod, alt, peso
        if alt < mais_baixo:
            mais_baixo = alt
            pessoa_mais_baixa = cod, alt, peso
        if peso < mais_magro:
            mais_magro = peso
            pessoa_mais_magra = cod, alt, peso
media_altura /= cont
media_peso /= cont

print("Media de peso: {}".format(media_peso))
print("Media de altura: {}".format(media_altura))
print("Id ** Altura ** Peso")
print("Mais alto: {}".format(pessoa_mais_alta))
print("Mais baixo: {}".format(pessoa_mais_baixa))
print("Mais gordo: {}".format(pessoa_mais_gorda))
print("Mais magro: {}".format(pessoa_mais_magra))
