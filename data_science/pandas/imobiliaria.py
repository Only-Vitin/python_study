import pandas as pd
from matplotlib import pyplot as plt

URL = (
    "https://raw.githubusercontent.com/"
    "alura-cursos/pandas-conhecendo-a-biblioteca/"
    "main/base-de-dados/aluguel.csv"
)
dados = pd.read_csv(URL, sep=";")
print(dados.head(5))
print()
print(dados.info())
print()

media_tipo = dados.groupby("Tipo")[["Valor"]].mean().sort_values("Valor")
media_tipo.plot(kind="barh", figsize=(14, 10), color="purple")
plt.show()
