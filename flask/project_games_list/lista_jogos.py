from flask import Flask, render_template, request, redirect


class ListaJogos():
    def __init__(self, nome, categoria, console, preco) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console
        self.preco = preco


lista_jogos = []

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos:', jogos=lista_jogos)

@app.route('/new')
def novo_jogo():
    return render_template('novo.html', titulo='Adicionar um novo jogo: ')
    
@app.route('/create', methods=['POST',])
def cria_jogo():
    nome =  request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    preco = request.form['preco']

    jogo = ListaJogos(nome, categoria, console, preco)
    lista_jogos.append(jogo)

    return redirect('/')

app.run()