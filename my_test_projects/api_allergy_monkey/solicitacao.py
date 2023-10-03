import requests

url = 'http://127.0.0.1:5000/exemplo'  # URL da sua API
params = {'nome': 'Vitin'}  # Dicionário de parâmetros

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()  # Converte a resposta JSON em um dicionário Python
    # Agora você pode acessar e usar os dados conforme necessário
    print(data)
else:
    print('Erro na solicitação GET:', response.status_code)