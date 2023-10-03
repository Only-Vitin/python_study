import pandas as pd
import json
import os

caminho = os.path.join('my_test_projects', 'api_allergy_monkey', 'bd.json')
with open(caminho, "r") as arquivo:
    dados = json.load(arquivo)

cadastro_df = pd.DataFrame(dados)
cadastro_df.set_index('id', inplace=True)
cadastro_df.reset_index(inplace=True)

par = '94835984'
result = cadastro_df.query('@par in id')
print(result)