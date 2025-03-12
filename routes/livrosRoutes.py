from flask import Blueprint, request, jsonify,render_template
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
            tema=dados["tema"],
            imagem=dados["imagem"]
        )

        livro.salvar()
        return jsonify({"mensagem": "Livro adicionado com sucesso!"}), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 400  # Retorna erro caso algo dê errado

@livros_blueprint.route('/deletar_livro', methods=['DELETE'])
def deletar_livro():
    try:
        dados = request.json  # Pegando os dados corretamente
        titulo = dados["titulo"]

        livro = livros.Livros(
            titulo=titulo, 
            autor=dados.get("autor"), 
            publicacao=dados.get("publicacao"), 
            tema=dados.get("tema"),
            imagem=dados.get("imagem")
        )

        livro.deletar(titulo)
        return jsonify({"mensagem": "Livro excluido com sucesso!"}), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 400  # Retorna erro caso algo dê errado

@livros_blueprint.route('/atualizar_livro', methods=['PUT'])
def atualizar_livro():
    try:
        dados = request.json  # Pegando os dados corretamente

        titulo_atual = dados["titulo"]        
        atualizar = dados.get("atualizar")
        autor=dados.get("autor"), 
        publicacao=dados.get("publicacao"), 
        tema=dados.get("tema"),
        imagem=dados.get("imagem")
        
        livro = livros.Livros(titulo=titulo_atual)

        livro.atualizar(titulo_atual, atualizar, autor, publicacao, tema, imagem)
        return jsonify({"mensagem": "Livro atualizado com sucesso!"}), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 400  # Retorna erro caso algo dê errado



@livros_blueprint.route('/listar_livros')
def listar_livros():
    livros_cadastrados = livros.buscar_todos()
    return jsonify(livros_cadastrados), 200

