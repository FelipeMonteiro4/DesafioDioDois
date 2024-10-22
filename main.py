total_de_vitorias = 11
total_de_derrotas = 10
resultado = total_de_vitorias - total_de_derrotas


def calculo():
    rank = "Ferro"

    if resultado >= 101:
        rank = "Imortal"

    if resultado >= 91 and resultado <= 100:
        rank = "Lendário"

    if resultado >= 81 and resultado <= 90:
        rank = "Diamante"

    if resultado >= 51 and resultado <= 80:
        rank = "Ouro"

    if resultado >= 21 and resultado <= 50:
        rank = "Prata"

    if resultado >= 11 and resultado <= 20:
        rank = "Bronze"

    print("O herói de saldo de " + str(total_de_vitorias) + " está no nível de " + rank)


calculo()
