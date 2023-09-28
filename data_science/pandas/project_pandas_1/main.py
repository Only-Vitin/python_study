from tabela_de_dados import TabelaDados

URL = (
    "https://raw.githubusercontent.com/"
    "alura-cursos/pandas-conhecendo-a-biblioteca/"
    "main/base-de-dados/aluguel.csv"
)

dados_imobiliaria = TabelaDados(URL)

print(dados_imobiliaria)
dados_imobiliaria.get_grafico_media("residencial")
dados_imobiliaria.get_grafico_percentual("residencial")
# print(dados_imobiliaria.get_informacoes('geral'))
# print(dados_imobiliaria.busca_parametro('Flamengo', 'Bairro'))
