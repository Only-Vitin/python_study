from registro import RegistroChegadaLog

dias_da_semana = (
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo",
)


def main():
    registro_chegada_log = RegistroChegadaLog()
    while True:
        operacao = input(
            "Digite 'c' para registrar chegada, 'h' para ver o histórico ou 'm' para calcular médias: "
        )

        if operacao == "c":
            usuario = input("Digite o nome do usuário: ")
            registro_chegada_log.adicionar_chegada(usuario)
            print(f"Registro de horário feito com sucesso - {usuario}\n")

        elif operacao == "h":
            for dia in dias_da_semana:
                print(f"{dia}:")
                for chegada in registro_chegada_log.registro_semanal[dia]:
                    print(chegada)
                print("\n")

        elif operacao == "m":
            medias = registro_chegada_log.calcular_tempo_medio()
            print("\nMédias dos horários por dia da semana:\n")
            for dia in dias_da_semana:
                print(f"{dia}: {registro_chegada_log.formatar_tempo(medias[dia])}")
            print()


if __name__ == "__main__":
    main()
