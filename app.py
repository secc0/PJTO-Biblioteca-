from flask import Flask, render_template, session
from routes.livrosRoutes import livros_blueprint
from routes.usuariosRoutes import usuarios_blueprint
from decorators.autenticacao import login_required, somente_admin
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SENHA")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/listar')
@login_required
def listar():
    usuario = session['user']
    return render_template('listar.html', usuario=usuario)

@app.route('/cadastro')
@login_required
@somente_admin()
def cadastro():
    return render_template('cadastro.html')


app.register_blueprint(livros_blueprint)
app.register_blueprint(usuarios_blueprint)

if __name__ == "__main__":
    app.run(debug=True)