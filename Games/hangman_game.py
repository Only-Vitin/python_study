from random import randint
from unidecode import unidecode

def jogar():
    inicializacao()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = ["_"]*len(palavra_secreta)
    chutes = []

    enforcou = False
    acertou = False
    erros = 0

    print(" ______\n|      |\n|      \n|      \n|      \n|")
    print("| ",' '.join(letras_acertadas), end="\n\n")
    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        chute = unidecode(chute)
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        
        if len(chute) == 1:
            if chute not in chutes:
                chutes.append(chute)

                if chute in unidecode(palavra_secreta):
                    marca_letras(palavra_secreta, chute, letras_acertadas)
                else:
                    erros += 1
                
                printa_forca(erros, letras_acertadas, chutes)
            else:
                print("Você já chutou essa letra!")
        else:
            chute_palavra = chute
            if chute_palavra == unidecode(palavra_secreta):
                acertou = True
            else:
                print("Essa não é a palavra secreta")
                erros += 1
                printa_forca(erros, letras_acertadas, chutes)
                continue
            
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    
def inicializacao():
    print(" ___________________________", end="\n\n")
    print("|    Boas vindas à Forca    |", end="\n")
    print(" ___________________________", end="\n")
    print("*** Você tem 7 tentativas ***", end="\n\n")
    
def carrega_palavra_secreta():
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        palavras_secretas = arquivo.readlines()
        palavra_secreta = palavras_secretas[randint(0, len(palavras_secretas)-1)]
        palavra_secreta = palavra_secreta.upper().strip()
    return palavra_secreta


def marca_letras(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == unidecode(letra):
            letras_acertadas[index] = letra
        index = index + 1

def printa_forca(erros, letras_acertadas, chutes):
    if erros == 0:
        print(" ______\n|      |\n|      \n|      \n|      \n|")
        print("| ",' '.join(letras_acertadas), end="\n\n")
    elif erros == 1:
        print(" ______\n|      |\n|      O\n|      \n|      \n|")
        print("| ",' '.join(letras_acertadas), end="\n\n")
    elif erros == 2:
        print(" ______\n|      |\n|      O\n|      | \n|      \n|")
        print("| ",' '.join(letras_acertadas), end="\n\n")
    elif erros == 3:
        print(" ______\n|      |\n|      O\n|      |\ \n|      \n|")
        print("| ",' '.join(letras_acertadas), end="\n\n")
    elif erros == 4:
        print(" ______\n|      |\n|      O\n|     /|\ \n|      \n|")
        print("| ",' '.join(letras_acertadas), end="\n\n")
    elif erros == 5:
        print(" ______\n|      |\n|      O\n|     /|\ \n|     / \n|")
        print("| ",' '.join(letras_acertadas), end="\n\n")
    elif erros == 6:
        print(" ______\n|      |\n|      O\n|     /|\ \n|     / \ \n|")
        print("| ",' '.join(letras_acertadas), end="\n\n")
        
    print("Chutes: ", ', '.join(chutes), '\n')

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       \n")
    
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print(" /                   \  ")
    print(" |   XXXX     XXXX   |    ")
    print(" |   XXXX     XXXX   |     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           \n")

if (__name__ == "__main__"):
    jogar()