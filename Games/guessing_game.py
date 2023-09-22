import random


def escolhe_nivel():
    print("Escolha o nível de dificuldade", end="\n")
    print("(1) Fácil  (2) Médio  (3) Difícil", end="\n")
    nivel = int(input("- "))
    print("")

    if nivel == 1:
        tentativas = 15
        pontos = 1500
        print("*** Nível 1 - Fácil ***")
        print(f"Sua pontuação inicial: {pontos}", end="\n")
        print("A cada rodada você perde 100 pontos", end="\n\n")
        return tentativas, pontos

    if nivel == 2:
        tentativas = 10
        pontos = 1000
        print("*** Nível 2 - Médio ***")
        print(f"Sua pontuação inicial: {pontos}", end="\n")
        print("A cada rodada você perde 100 pontos", end="\n\n")
        return tentativas, pontos

    if nivel == 3:
        tentativas = 5
        pontos = 500
        print("*** Nível 3 - Difícil ***")
        print(f"Sua pontuação inicial: {pontos}", end="\n")
        print("A cada rodada você perde 100 pontos", end="\n\n")
        return tentativas, pontos

    return False, False


def jogar():
    print("_____________________________", end="\n\n")
    print("Boas vindas ao jogo de adivinhação", end="\n")
    print("_____________________________", end="\n\n")
    print("Tente adivinhar o número secreto", end="\n\n")

    numero_secreto = random.randrange(1, 101)
    tentativas = None
    pontos = None

    tentativas, pontos = escolhe_nivel()

    while tentativas > 0:
        print(f"Você tem {tentativas} tentativas", end="\n")
        tentativas = tentativas - 1

        chute = int(input("Digite um número entre 1 e 100: "))
        print("")

        if chute < 1 or chute > 100:
            print("! Por favor, digite um número entre 1 e 100 !", end="\n\n")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("************************", end="\n")
            print("Parabéns, Você acertou !", end="\n")
            print("************************", end="\n")
        elif maior:
            print("Que pena, você errou", end="\n")
            print("Seu chute foi MAIOR do que o número secreto", end="\n\n")
        elif menor:
            print("Que pena, você errou", end="\n")
            print("Seu chute foi MENOR do que o número secreto", end="\n\n")

        pontos = pontos - 100

    print("Fim de Jogo!", end="\n")
    print("O número era: ", numero_secreto, end="\n")
    print(f"Sua pontuação final foi: {pontos} pontos", end="\n")


if __name__ == "__main__":
    jogar()
