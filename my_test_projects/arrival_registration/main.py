from registro import RegistroChegadaLog


def exibir_ajuda() -> None:
    print("Opções disponíveis:")
    print("  'c' - Registrar chegada")
    print("  'h' - Histórico de chegadas")
    print("  'm' - Médias dos horários")
    print("  'g' - Gerar gráfico")


def main() -> None:
    registro_chegada_log = RegistroChegadaLog()

    while True:
        operacao: str = input("Digite a operação desejada ('help' para ajuda): ")

        if operacao == "c":
            usuario = input("Digite o nome do usuário: ")
            registro_chegada_log.adicionar_chegada(usuario)
            print(f"Registro de horário feito com sucesso - {usuario}\n")

        elif operacao == "h":
            dia = input("Qual dia você deseja ver ? ")
            print(registro_chegada_log.historico_dia(dia))

        elif operacao == "m":
            print(registro_chegada_log.retorna_media())

        elif operacao == "g":
            registro_chegada_log.mostra_grafico()

        elif operacao == "help":
            exibir_ajuda()

        else:
            print("Operação inválida. Digite 'h' para ajuda.")


if __name__ == "__main__":
    main()
