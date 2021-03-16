"""Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer
um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que
se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número i
ndeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
- necessita da esfera;
- necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero
encerra o programa. Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""
esfera = limpeza = cabo_conector = quebrado = quant_mouses = 0

while True:
    condicao = str(input("1- necessita da esfera  \n"
                         "2- necessita de limpeza  \n"
                         "3- necessita troca do cabo ou conector \n"
                         "4- quebrado ou inutilizado \n"
                         "0- zero para sair\n"
                         "Digite a condicao do mouse: "))
    if condicao == "0":
        print("Programa encerrado! Obrigado!")
        break
    elif condicao not in ("1", "2", "3", "4"):
        print("Condicao Invalida!, tente novamente!\n\n")
        continue
    else:
        if condicao == "1":
            esfera += 1
        elif condicao == "2":
            limpeza += 1
        elif condicao == "3":
            cabo_conector += 1
        elif condicao == "4":
            quebrado += 1
        quant_mouses += 1
        print("Obrigado pelo seu voto!")

print("*** Resulatdos ***")
print("1 - necessita da esfera - {} - {:.2%}\n"
      "2 - necessita de limpeza - {} - {:.2%} \n"
      "3 - necessita troca do cabo ou conector - {} - {:.2%}\n"
      "4 - quebrado ou inutilizado - {} - {:.2%}\n"
      .format(esfera, (esfera / quant_mouses), limpeza,
              (limpeza / quant_mouses), cabo_conector, (cabo_conector / quant_mouses), quebrado,
              (quebrado / quant_mouses)))

print("Total de mouses = {}".format(quant_mouses))


"""Falta apenas formatar as strings. Ler sobre isso. Fazer formatação manual."""