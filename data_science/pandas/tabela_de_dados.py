import pandas as pd
from pandas.core.frame import DataFrame
from typing import List
from matplotlib import pyplot as plt
from constantes import IMOVEIS_COMERCIAIS

class TabelaDados:

    def __init__(self, URL) -> None:
        self.dados = self.define_dados(URL)
        self.IMOVEIS_COMERCIAIS: List[str] = IMOVEIS_COMERCIAIS
        self.dados_res: DataFrame = self.dados.query('@self.IMOVEIS_COMERCIAIS not in Tipo')
        self.dados_com: DataFrame = self.dados.query('@self.IMOVEIS_COMERCIAIS in Tipo')

    def __str__(self) -> str:
        return '\n' + f'{self.dados}' + '\n'
    
    def define_dados(self, URL: str) -> DataFrame:
        dados = pd.read_csv(URL, sep=";")
        dados = dados.fillna(0)
        return dados

    def _processar_dados(self, dados: DataFrame, flag: str) -> DataFrame:
        if flag == 'residencial':
            dados_filtrados = dados.query('@IMOVEIS_COMERCIAIS not in Tipo')
        elif flag == 'comercial':
            dados_filtrados = dados.query('@IMOVEIS_COMERCIAIS in Tipo')
        elif flag == 'geral':
            dados_filtrados = dados
        else:
            raise ValueError("Essa flag não existe, somente 'residencial', 'comercial' e 'geral'")
        
        return dados_filtrados

    def get_grafico_media(self, flag: str) -> None:
        dados_filtrados = self._processar_dados(self.dados, flag)
        media_tipo = dados_filtrados.groupby("Tipo")[["Valor"]].mean().sort_values("Valor")
        
        media_tipo.plot(kind="barh",figsize=(9, 5), color="purple", fontsize=10)

        fig_manager = plt.get_current_fig_manager()
        if fig_manager.window:
            fig_manager.window.wm_geometry("+%d+%d" % (400, 150))

        plt.title(f"Média conforme o tipo de imóvel - {flag.title()}: ", fontsize=14, fontweight='bold')
        plt.subplots_adjust(left=0.278, right=0.96, bottom=0.126, top=0.910)
        plt.xlabel('Media dos Valores')
        plt.ylabel('Tipos de Imóveis')
        plt.show()
        
    def get_grafico_percentual(self, flag: str) -> None:
        dados_filtrados = self._processar_dados(self.dados, flag)
        percentual_tipo = dados_filtrados.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')
        
        percentual_tipo.plot(kind="bar",figsize=(9, 7), color="red", fontsize=10)

        fig_manager = plt.get_current_fig_manager()
        if fig_manager.window:
            fig_manager.window.wm_geometry("+%d+%d" % (400, 20))

        plt.title(f"Percentual dos tipos de imóveis - {flag.title()} : ", fontsize=14, fontweight='bold')
        plt.subplots_adjust(left=0.093, right=0.96, bottom=0.358, top=0.926)
        plt.xlabel('Tipos de Imóveis')
        plt.ylabel('Percentual')
        plt.show()
    
    def get_informacoes(self, flag: str):
        dados_filtrados = self._processar_dados(self.dados, flag)
        infos = {}
        infos['CINCO PRIMEIRAS LINHAS'] = dados_filtrados.head(5)
        infos['CINCO ULTIMAS LINHAS'] = dados_filtrados.tail(5)
        infos['DESCRIÇÕES GERAIS'] = dados_filtrados.describe()
        infos['COLUNAS'] = dados_filtrados.columns
        infos['QUANTIDADE LINHAS E COLUNAS'] = dados_filtrados.shape
        infos['TIPO DAS COLUNAS'] = dados_filtrados.dtypes

        informacoes_formatadas = ""
        for chave, valor in infos.items():
            informacoes_formatadas += chave + ":\n" + str(valor) + '\n\n'

        return informacoes_formatadas

    def busca_parametro(self, parametro: str, coluna: str) -> DataFrame:
        self.par = parametro
        return self.dados.query(f'@self.par in {coluna}')