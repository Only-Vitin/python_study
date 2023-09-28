from typing import List, Dict

import pandas as pd
from pandas.core.frame import DataFrame
from matplotlib import pyplot as plt

from constantes import imoveis_comerciais


class TabelaDados:
    def __init__(self, url) -> None:
        self.par: str = None
        self.dados: DataFrame = self.define_dados(url)
        self.imoveis_comerciais: List[str] = imoveis_comerciais
        self.dados_res: DataFrame = self.dados.query(
            "@self.imoveis_comerciais not in Tipo"
        )
        self.dados_com: DataFrame = self.dados.query("@self.imoveis_comerciais in Tipo")

    def __str__(self) -> str:
        return "\n" + f"{self.dados}" + "\n"

    def define_dados(self, url: str) -> DataFrame:
        dados = pd.read_csv(url, sep=";")
        dados = dados.fillna(0)
        return dados

    def _processar_dados(self, dados: DataFrame, flag: str) -> DataFrame:
        if flag == "residencial":
            dados_filtrados: DataFrame = dados.query(
                "@self.imoveis_comerciais not in Tipo"
            )
        elif flag == "comercial":
            dados_filtrados: DataFrame = dados.query("@self.imoveis_comerciais in Tipo")
        elif flag == "geral":
            dados_filtrados: DataFrame = dados
        else:
            raise ValueError(
                "Essa flag não existe, somente 'residencial', 'comercial' e 'geral'"
            )
        return dados_filtrados

    def get_grafico_media(self, flag: str) -> None:
        dados_filtrados = self._processar_dados(self.dados, flag)
        media_tipo = (
            dados_filtrados.groupby("Tipo")[["Valor"]].mean().sort_values("Valor")
        )

        media_tipo.plot(kind="barh", figsize=(9, 5), color="purple", fontsize=10)

        fig_manager = plt.get_current_fig_manager()
        if fig_manager.window:
            fig_manager.window.wm_geometry(f"+{400}+{150}")

        plt.title(
            f"Média conforme o tipo de imóvel - {flag.title()}: ",
            fontsize=14,
            fontweight="bold",
        )
        plt.subplots_adjust(left=0.278, right=0.96, bottom=0.126, top=0.910)
        plt.xlabel("Media dos Valores")
        plt.ylabel("Tipos de Imóveis")
        plt.show()

    def get_grafico_percentual(self, flag: str) -> None:
        dados_filtrados = self._processar_dados(self.dados, flag)
        percentual_tipo = (
            dados_filtrados.Tipo.value_counts(normalize=True)
            .to_frame()
            .sort_values("Tipo")
        )

        percentual_tipo.plot(kind="bar", figsize=(9, 7), color="red", fontsize=10)

        fig_manager = plt.get_current_fig_manager()
        if fig_manager.window:
            fig_manager.window.wm_geometry(f"+{400}+{20}")

        plt.title(
            f"Percentual dos tipos de imóveis - {flag.title()} : ",
            fontsize=14,
            fontweight="bold",
        )
        plt.subplots_adjust(left=0.093, right=0.96, bottom=0.358, top=0.926)
        plt.xlabel("Tipos de Imóveis")
        plt.ylabel("Percentual")
        plt.show()

    def get_informacoes(self, flag: str) -> str:
        dados_filtrados = self._processar_dados(self.dados, flag)
        infos: Dict[str, DataFrame] = {}
        infos["CINCO PRIMEIRAS LINHAS"] = dados_filtrados.head(5)
        infos["CINCO ULTIMAS LINHAS"] = dados_filtrados.tail(5)
        infos["DESCRIÇÕES GERAIS"] = dados_filtrados.describe()
        infos["COLUNAS"] = dados_filtrados.columns
        infos["QUANTIDADE LINHAS E COLUNAS"] = dados_filtrados.shape
        infos["TIPO DAS COLUNAS"] = dados_filtrados.dtypes

        informacoes_formatadas = ""
        for chave, valor in infos.items():
            informacoes_formatadas += chave + ":\n" + str(valor) + "\n\n"

        return informacoes_formatadas

    def busca_parametro(self, parametro: str, coluna: str) -> DataFrame:
        self.par = parametro
        return self.dados.query(f"@self.par in {coluna}")
