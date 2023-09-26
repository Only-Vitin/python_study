import pandas as pd

URL = (
    "https://raw.githubusercontent.com/"
    "alura-cursos/pandas-conhecendo-a-biblioteca/"
    "main/base-de-dados/aluguel.csv"
)
dados = pd.read_csv(URL, sep=";")
print(dados.head(10))
print(dados.info())
