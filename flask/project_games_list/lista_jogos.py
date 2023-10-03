from flask import Flask, render_template, request, redirect, session, flash


class ListaJogos():
    def __init__(self, nome, categoria, console, preco) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console
        self.preco = preco


lista_jogos = []

app = Flask(__name__)
app.secret_key = 'abcd'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos:', jogos=lista_jogos)

@app.route('/new')
def novo_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Por favor efetue o login')
        return redirect('/login')
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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'bejobejo' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso')
        return redirect('/')
    else:
        flash('Usuário não foi logado')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')

app.run()