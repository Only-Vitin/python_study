def jogar():
    print("_____________________________", end="\n\n")
    print("Boas vindas à Forca", end="\n")
    print("_____________________________", end="\n\n")

    palavra_secreta = "alface"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")

        index = 1
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}".format(chute,index))
            index = index + 1

        print("Jogando...")
    print("Fim de Jogo")
    
if (__name__ == "__main__"):
    jogar()