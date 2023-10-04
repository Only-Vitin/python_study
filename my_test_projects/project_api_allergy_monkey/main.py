from flask_restful import Api
from flask import Flask

from route_cadastro import Cadastro


app = Flask('Banana Allergy Monkey API')
app.config['JSON_SORT_KEYS'] = False
api = Api(app)

api.add_resource(Cadastro, '/cadastro')


if __name__ == '__main__':
    app.run()