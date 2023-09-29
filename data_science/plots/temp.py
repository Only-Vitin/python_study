import os
import pandas as pd

caminho_arquivo = os.path.join('data_science', 'plots', 'canadian_immegration_data.csv')

df = pd.read_csv(caminho_arquivo)
df.set_index('Country', inplace=True)

anos = list(map(str, range(1980, 2014)))
brasil = df.loc['Brazil', anos]

brasil_dict = {'Ano' : brasil.index.tolist(), 'Imigrantes' : brasil.values.tolist()}
df_brasil = pd.DataFrame(brasil_dict)

print(df_brasil)