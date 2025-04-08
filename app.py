from flask import Flask, render_template
from routes.livrosRoutes import livros_blueprint
from routes.usuariosRoutes import usuarios_blueprint
from decorators.autenticacao import login_usuario, somente_admin

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/listar')
@login_usuario()
def listar():
    return render_template('listar.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


app.register_blueprint(livros_blueprint)
app.register_blueprint(usuarios_blueprint)

if __name__ == "__main__":
    app.run(debug=True)