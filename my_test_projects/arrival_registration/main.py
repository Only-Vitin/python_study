from funcoes import opera


def main() -> None:
    while True:
        print()
        operacao: str = input("Digite a operação desejada ('help' para ajuda): ")

        opera(operacao)

if __name__ == "__main__":
    main()
