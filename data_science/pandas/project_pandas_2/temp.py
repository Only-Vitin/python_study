import os
import numpy as np
import pandas as pd


''' Criar arquivo puxando de uma URL
dados = pd.read_json('https://caelum-online-public.s3.amazonaws.com/2928-transformacao-manipulacao-dados/dados.json')
dados.to_json(caminho_arquivo)'''

# Definindo o caminho para o arquivo
caminho_arquivo_dados = os.path.join('data_science', 'pandas', 'project_pandas_2', 'dados_hospedagem.json')
caminho_arquivo_csv = os.path.join('data_science', 'pandas', 'project_pandas_2', 'dados_formatados.csv')

#Lendo dados dos arquivos json
dados = pd.read_json(caminho_arquivo_dados)
dados = pd.json_normalize(dados['info_moveis'])

#Tirando as informações das colunas selecionadas da lista
colunas = list(dados.columns)
dados = dados.explode(colunas[3:])
dados.reset_index(inplace=True, drop=True)

#Mudando colunas para int64
col_numericas = ['max_hospedes', 'quantidade_banheiros', 'quantidade_quartos', 'quantidade_camas']
dados[col_numericas] = dados[col_numericas].astype(np.int64)

#Mudando colunas para float64
dados['preco'] = dados['preco'].apply(lambda x: x.replace('$', '').replace(',', '').strip())
dados['preco'] = dados['preco'].astype(np.float64)
dados[['taxa_deposito','taxa_limpeza']] = dados[['taxa_deposito','taxa_limpeza']].applymap(lambda x: float(x.replace('$', '').replace(',','').strip()))
dados[['taxa_deposito','taxa_limpeza']] = dados[['taxa_deposito','taxa_limpeza']].astype(np.float64)

# print(dados.dtypes)
# print(dados.iloc[:, 0:5].head(10))
# print(dados[['preco', 'taxa_deposito', 'taxa_limpeza']])

####################################################################################################
#Colunas textuais

#Tokenização
dados['descricao_local'] = dados['descricao_local'].str.lower()
dados['descricao_local'] = dados['descricao_local'].str.replace('[^a-zA-Z0-9\-\']', ' ', regex=True)
dados['descricao_local'] = dados['descricao_local'].str.replace('(?<!\w)-(?!\w)', ' ', regex=True)
dados['descricao_local'] = dados['descricao_local'].str.split()

dados['comodidades'] = dados['comodidades'].str.replace('\{|}|\"','',regex=True)
dados['comodidades'] = dados['comodidades'].str.split(',')

dados.to_csv(caminho_arquivo_csv)