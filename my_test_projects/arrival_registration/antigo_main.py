import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from registro import RegistroChegadaLog
from registro import dias_da_semana

def exibir_ajuda():
    print("Opções disponíveis:")
    print("  'c' - Registrar chegada")
    print("  'h' - Histórico de chegadas")
    print("  'm' - Médias dos horários")
    print("  'g' - Gerar gráfico")

def main():
    registro_chegada_log = RegistroChegadaLog()

    while True:
        operacao = input("Digite a operação desejada ('help' para ajuda): ")

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
            medias = registro_chegada_log.retorna_tempo_medio()
            print("\nMédias dos horários por dia da semana:\n")
            for dia in dias_da_semana:
                media = medias.get(dia, 0)
                print(f"{dia}: {registro_chegada_log.formatar_tempo(media)}")
            print()

        elif operacao == "g":
            horarios = [0]*5
            medias = registro_chegada_log.retorna_tempo_medio()
            for i in range(len(dias_da_semana)):
                horarios[i] = (f"{registro_chegada_log.formatar_tempo(medias[dias_da_semana[i]])}")
            horarios_dt = [datetime.strptime(hora, "%H:%M:%S") for hora in horarios]
            lista = list(zip(dias_da_semana, horarios_dt))
            df = pd.DataFrame(lista, columns=['Dias da semana', 'Horários'])

            df.plot(x='Dias da semana', y='Horários', kind='line', figsize=(9, 5), color="purple", fontsize=10)
            plt.xlabel('Dias da Semana', fontsize=12)
            plt.ylabel('Horários', fontsize=12)

            plt.title("Média dos horários por dia da semana", fontsize=16, fontweight='bold')
            plt.subplots_adjust(left=0.278, right=0.96, bottom=0.126, top=0.910)

            plt.show()

        elif operacao == "help":
            exibir_ajuda()

        else:
            print("Operação inválida. Digite 'h' para ajuda.")

if __name__ == "__main__":
    main()
