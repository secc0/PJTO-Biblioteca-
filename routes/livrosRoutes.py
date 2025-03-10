from flask import Blueprint, request, jsonify
from models import livros

livros_blueprint = Blueprint('livros', __name__, url_prefix='/livros')

@livros_blueprint.route('/')
def homeLivros():
    return "<p>Hello, World!</p>"


@livros_blueprint.route('/adicionar_livro', methods=['POST'])
def adicionar_livro():
    try:
        dados = request.json  # Pegando os dados corretamente
        livro = livros.Livros(
            titulo=dados["titulo"], 
            autor=dados["autor"], 
            publicacao=dados["publicacao"], 
            tema=dados["tema"]
        )

        livro.salvar()
        return jsonify({"mensagem": "Livro adicionado com sucesso!"}), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 400  # Retorna erro caso algo dê errado
