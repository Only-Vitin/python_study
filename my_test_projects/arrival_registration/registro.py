import csv
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
from constantes import caminho_arquivo

dias_da_semana = (
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira"
)

class RegistroChegada:
    def __init__(self) -> None:
        self.registro_tempo: datetime = self.obter_tempo_atual()
        self.dia_da_semana: str = self.obter_dia_da_semana()
        self.data: str = self.obter_data()
        self.hora: str = self.obter_hora()

    def obter_tempo_atual(self) -> datetime:
        return datetime.today()

    def obter_dia_da_semana(self) -> str:
        return dias_da_semana[self.registro_tempo.weekday()]

    def obter_data(self) -> str:
        data = self.registro_tempo.strftime('%d/%m/%Y')
        return data

    def obter_hora(self) -> str:
        hora = self.registro_tempo.strftime("%H:%M:%S")
        return hora
    
class RegistroChegadaLog:
    def __init__(self) -> None:
        self.registro_semanal = {dia: [] for dia in dias_da_semana}

    def __str__(self) -> str:
        resultado: str = ""
        for dia in dias_da_semana:
            resultado += (
                f"{dia}:" f"{self.formatar_tempo(self.retorna_tempo_medio()[dia])}"
            )
        return resultado
    
    def adicionar_chegada(self, usuario) -> None:
        registro = RegistroChegada()
        chegada_info: str = (
            f"{registro.dia_da_semana},{registro.data},{registro.hora},{usuario}"
        )
        with open(caminho_arquivo, mode="a", newline="") as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv, delimiter=' ', quoting=csv.QUOTE_MINIMAL, quotechar='|')
            escritor_csv.writerow([chegada_info])

    def historico_dia(self, parametro: str):
        df = pd.read_csv(caminho_arquivo)
        if parametro == 'todos':
            return df
        else:
            self.par = parametro
            resultado = df.query('Dias == @self.par')
            return resultado
    
    def retorna_media(self):
        df = pd.read_csv(caminho_arquivo)
        df["Hora"] = pd.to_datetime(df["Hora"], format="%H:%M:%S")
        media = df.groupby("Dias")[["Hora"]].mean()
        media["Hora"] = media["Hora"].apply(lambda x: x.strftime("%H:%M:%S"))
        media.rename(columns={"Hora": "Medias"}, inplace=True)
        media.reset_index(inplace=True)

        ordem_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
        media['Dias'] = pd.Categorical(media['Dias'], categories=ordem_semana, ordered=True)
        media = media.sort_values('Dias')

        return media
    
    def mostra_grafico(self):
        media = self.retorna_media()
        media["Medias"] = pd.to_datetime(media["Medias"], format="%H:%M:%S")
        media.plot(x='Dias', y='Medias', kind='line', figsize=(9, 5), color="purple", fontsize=10)

        fig_manager = plt.get_current_fig_manager()
        if fig_manager.window:
            fig_manager.window.wm_geometry("+%d+%d" % (400, 150))

        plt.title(f"Média dos horários: ", fontsize=14, fontweight='bold')
        plt.subplots_adjust(left=0.278, right=0.96, bottom=0.126, top=0.910)
        plt.xlabel('Dias da semana')
        plt.ylabel('Horários')
        plt.show()