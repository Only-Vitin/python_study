import os
import csv
from typing import Tuple
from datetime import datetime

import pandas as pd
from pandas.core.frame import DataFrame
from matplotlib import pyplot as plt

dias_da_semana: Tuple[str] = (
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
)

caminho_arquivo: str = os.path.join(
    "my_test_projects", "arrival_registration", "horarios_chegada.csv"
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
        data: str = self.registro_tempo.strftime("%d/%m/%Y")
        return data

    def obter_hora(self) -> str:
        hora: str = self.registro_tempo.strftime("%H:%M:%S")
        return hora


class RegistroChegadaLog:
    def __init__(self) -> None:
        self.par: str = None

    def __str__(self) -> str:
        df = pd.read_csv(caminho_arquivo)
        return df

    def adicionar_chegada(self, usuario) -> None:
        registro = RegistroChegada()
        chegada_info: str = (
            f"{registro.dia_da_semana},{registro.data},{registro.hora},{usuario}"
        )
        with open(
            caminho_arquivo, mode="a", newline="", encoding="utf-8"
        ) as arquivo_csv:
            escritor_csv = csv.writer(
                arquivo_csv, delimiter=" ", quoting=csv.QUOTE_MINIMAL, quotechar="|"
            )
            escritor_csv.writerow([chegada_info])

    def historico_dia(self, parametro: str) -> DataFrame:
        df = pd.read_csv(caminho_arquivo)
        if parametro == "Todos":
            return df
        self.par = parametro
        resultado = df.query("Dias == @self.par")
        return resultado

    def retorna_media(self) -> DataFrame:
        df = pd.read_csv(caminho_arquivo)
        df["Hora"] = pd.to_datetime(df["Hora"], format="%H:%M:%S")
        media = df.groupby("Dias")[["Hora"]].mean()
        media["Hora"] = media["Hora"].apply(lambda x: x.strftime("%H:%M:%S"))
        media.rename(columns={"Hora": "Medias"}, inplace=True)
        media.reset_index(inplace=True)

        media["Dias"] = pd.Categorical(
            media["Dias"], categories=dias_da_semana, ordered=True
        )
        media = media.sort_values("Dias")

        return media

    def mostra_grafico(self) -> None:
        media = self.retorna_media()
        media["Medias"] = pd.to_datetime(media["Medias"], format="%H:%M:%S")
        media.plot(
            x="Dias",
            y="Medias",
            kind="line",
            figsize=(9, 5),
            color="purple",
            fontsize=10,
        )

        fig_manager = plt.get_current_fig_manager()
        if fig_manager.window:
            fig_manager.window.wm_geometry(f"+{400}+{150}")

        plt.title("Média dos horários: ", fontsize=14, fontweight="bold")
        plt.subplots_adjust(left=0.278, right=0.96, bottom=0.126, top=0.910)
        plt.xlabel("Dias da semana")
        plt.ylabel("Horários")
        plt.show()
