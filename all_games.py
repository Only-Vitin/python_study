import game_adivinhação
import game_forca

print("_____________________________", end="\n\n")
print("Escolha um jogo", end="\n")
print("_____________________________", end="\n\n")
print("(1)Adivinhação  (2)Forca", end="\n")
jogo = int(input("- "))
print("")

if (jogo == 1):
    print("Jogando Adivinhação")
    game_adivinhação.jogar()
elif (jogo == 2):
    print("Jogando Forca")
    game_forca.jogar()