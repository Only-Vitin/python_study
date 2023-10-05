import pandas as pd
from flask_restful import Resource
import bcrypt
from flask import jsonify, request, make_response
from config_mysql import connection

from _constants import TABLE_REGISTER


class Register(Resource):
    def get(self):
        try:
            register_df = pd.read_sql_table(TABLE_REGISTER, connection)
            user = request.args.get("user")
            result = register_df.query("@user in user")

            if result.empty:
                return make_response(jsonify({"message": f"Usuário '{user}' não encontrado"}), 404)
            else:
                result_dict = result.to_dict(orient="records")
        except KeyError as e:
            if "boolean index" in str(e):
                return make_response(jsonify({"message": "Verifique os parâmetros"}), 400)
        else:
            return make_response(jsonify(result_dict))

    def post(self):
        data_json = request.json
        passwd = data_json["passwd"]
        
        data_json["passwd"] = bcrypt.hashpw(passwd, bcrypt.gensalt())

        register_df = pd.read_sql_table(TABLE_REGISTER, connection)
        data_df = pd.DataFrame([data_json])
        register_df = pd.concat([register_df, data_df], ignore_index=True)

        register_df.to_sql(TABLE_REGISTER, connection, if_exists="replace", index=False)
        return make_response(jsonify({"message": "Usuário cadastrado com sucesso"}), 200)

class VerificaLogin(Resource):
    def get(self):
        data_json = request.json
        register_df = pd.read_sql_table(TABLE_REGISTER, connection)
        user = data_json["user"]
        passwd = data_json["passwd"]

        result = register_df.query("@user in user")

        if result.empty:
            return False
        else:
            hash = result.iloc[0, 3]
            print(hash)
            if bcrypt.hashpw(passwd.encode('utf-8'), hash.encode('utf-8')) == hash.encode('utf-8'):
                return True
            return False

