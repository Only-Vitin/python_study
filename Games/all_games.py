import guessing_game
import hangman_game

print("_____________________________", end="\n\n")
print("Escolha um jogo", end="\n")
print("_____________________________", end="\n\n")
print("(1) Adivinhação  (2) Forca", end="\n")
jogo = int(input("- "))
print("")

if jogo == 1:
    print("Jogando Adivinhação")
    guessing_game.jogar()
elif jogo == 2:
    print("Jogando Forca")
    hangman_game.jogar()
