import guessing_game
import hangman_game


print("_____________________________", end="\n\n")
print("Escolha um jogo", end="\n")
print("_____________________________", end="\n\n")
print("(1) Adivinhação  (2) Forca", end="\n")

jogo = int(input("- "))
print(end="\n")

if jogo == 1:
    print("Jogando Adivinhação", end="\n")
    guessing_game.jogar()
elif jogo == 2:
    print("Jogando Forca", end="\n")
    hangman_game.jogar()
