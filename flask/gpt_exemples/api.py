from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Dados de exemplo em uma lista de tarefas
tarefas = {
    1: {'titulo': 'Estudar Flask-RESTful'},
    2: {'titulo': 'Construir uma API RESTful'},
}

# Parser para analisar as solicitações JSON
parser = reqparse.RequestParser()
parser.add_argument('titulo', type=str, required=True, help='O título da tarefa é obrigatório.')

class TarefaResource(Resource):
    def get(self, tarefa_id):
        if tarefa_id in tarefas:
            return tarefas[tarefa_id]
        else:
            return {'mensagem': 'Tarefa não encontrada'}, 404

    def put(self, tarefa_id):
        args = parser.parse_args()
        tarefas[tarefa_id] = {'titulo': args['titulo']}
        return tarefas[tarefa_id], 201

    def delete(self, tarefa_id):
        if tarefa_id in tarefas:
            del tarefas[tarefa_id]
            return {'mensagem': 'Tarefa excluída com sucesso'}, 204
        else:
            return {'mensagem': 'Tarefa não encontrada'}, 404

api.add_resource(TarefaResource, '/tarefa/<int:tarefa_id>')

if __name__ == '__main__':
    app.run(debug=True)
