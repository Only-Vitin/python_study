import pandas as pd
from flask_restful import Resource
from flask_bcrypt import generate_password_hash
from flask import jsonify, request, make_response
from config_mysql import connection

from _constantes import TABELA_CADASTRO


class Cadastro(Resource):
    def get(self):
        cadastro_df = pd.read_sql_table(TABELA_CADASTRO, connection)
        user = request.args.get("user")
        print(user)
        result = cadastro_df.query("@user in usuario")

        if result.empty:
            return make_response(jsonify({"message": "Usuário não encontrado"}), 404)

        result_dict = result.to_dict(orient="records")
        result_dict["senha"] = result_dict["senha"]
        return make_response(jsonify(result_dict))

    def post(self):
        dados_json = request.json
        dados_json["senha"] = generate_password_hash(dados_json["senha"]).decode(
            "utf-8"
        )
        cadastro_df = pd.read_sql_table(TABELA_CADASTRO, connection)
        dados_df = pd.DataFrame([dados_json])
        cadastro_df = pd.concat([cadastro_df, dados_df], ignore_index=True)

        cadastro_df.to_sql(
            TABELA_CADASTRO, connection, if_exists="replace", index=False
        )
        return make_response(
            jsonify({"message": "Usuário cadastrado com sucesso"}), 200
        )
