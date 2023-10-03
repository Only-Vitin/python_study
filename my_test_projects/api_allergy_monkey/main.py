from flask import Flask, jsonify, request, make_response
import pandas as pd
import json
import os


caminho = os.path.join('my_test_projects', 'api_allergy_monkey', 'bd.json')
with open(caminho, "r") as arquivo:
    dados = json.load(arquivo)

cadastro_df = pd.DataFrame(dados)


app = Flask('Banana Allergy Monkey API')

@app.route('/cadastro', methods=['GET'])
def get_cadastro():
    nome = request.args.get('nome')
    result = cadastro_df.query(f"@nome == '{nome}'")
    result = result.to_json()
    print(result)

    return jsonify(result)

app.run()