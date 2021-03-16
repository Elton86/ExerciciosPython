"""ma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de
organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser
aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser
armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de
cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

windows_server = unix = linux = netware = mac_os = outro = soma_votos = 0

while True:
    voto = str(input("1 - Windows Server\n"
                     "2 - Unix\n"
                     "3 - Linux\n"
                     "4 - Netware\n"
                     "5 - Mac OS\n"
                     "6 - Outro\n"
                     "0 - Sair\n"
                     "Digite seu voto: "))
    if voto == "0":
        print("Programa encerrado! Obrigado!")
        break
    elif voto not in ("1", "2", "3", "4", "5", "6"):
        print("Voto inválido, tente novamente!\n\n")
        continue
    else:
        if voto == "1":
            windows_server += 1
        elif voto == "2":
            unix += 1
        elif voto == "3":
            linux += 1
        elif voto == "4":
            netware += 1
        elif voto == "5":
            mac_os += 1
        elif voto == "6":
            outro += 1
        soma_votos += 1
        print("Obrigado pelo seu voto!")

print("*** Resulatdos ***")
print("Windows Server \t {} \t {:.2%}\n"
      "Unix \t\t\t{} \t {:.2%} \n"
      "Linux \t\t\t{} \t {:.2%}\n"
      "Netware \t\t{} \t {:.2%}\n"
      "Mac OS \t\t\t{} \t {:.2%}\n"
      "Outros \t\t\t{} \t {:.2%}\n".format(windows_server, (windows_server / soma_votos), unix,
                                           (unix / soma_votos), linux, (linux / soma_votos), netware,
                                           (netware / soma_votos), mac_os, (mac_os / soma_votos),
                                           outro, (outro / soma_votos)))

print("Total de votos = {}".format(soma_votos))
