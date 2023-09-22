from typing import Dict

from registro import RegistroChegadaLog
from registro import dias_da_semana


def main() -> None:
    registro_chegada_log = RegistroChegadaLog()
    while True:
        operacao: str = input(
            "Digite 'c' para registrar chegada, 'h' para histórico "
            "ou 'm' para médias: "
        )

        if operacao == "c":
            usuario: str = input("Digite o nome do usuário: ")
            registro_chegada_log.adicionar_chegada(usuario)
            print(f"Registro de horário feito com sucesso - {usuario}\n")

        elif operacao == "h":
            for dia in dias_da_semana:
                print(f"{dia}:")
                for chegada in registro_chegada_log.registro_semanal[dia]:
                    print(chegada)
                print("\n")

        elif operacao == "m":
            medias: Dict[str, int] = registro_chegada_log.calcular_tempo_medio()
            print("\nMédias dos horários por dia da semana:\n")
            for dia in dias_da_semana:
                print(f"{dia}: " f"{registro_chegada_log.formatar_tempo(medias[dia])}")
            print()


if __name__ == "__main__":
    main()
