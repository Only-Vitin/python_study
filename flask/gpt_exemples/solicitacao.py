import requests

url = 'http://127.0.0.1:5000/tarefa/1'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Converte a resposta JSON em um dicionário Python
    # Agora você pode acessar e usar os dados conforme necessário
    print(data)
else:
    print('Erro na solicitação GET:', response.status_code)
