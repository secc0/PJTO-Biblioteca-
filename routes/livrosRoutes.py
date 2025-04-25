from flask import Blueprint, request, jsonify, redirect, url_for
from controllers.livrosController import (
    homeLivros,
    adicionar_livro,
    deletar_livro,
    atualizar_livro,
    listar_livros,
    listar_um_livro
)
from decorators.autenticacao import login_required, somente_admin

livros_blueprint = Blueprint('livros', __name__, url_prefix='/livros')

@livros_blueprint.route('/adicionar_livro', methods=['POST'])
@login_required
@somente_admin()
def adicionar():
    return adicionar_livro()

@livros_blueprint.route('/deletar_livro', methods=['DELETE'])
@login_required
@somente_admin()
def deletar():
    return deletar_livro()

@livros_blueprint.route('/atualizar_livro', methods=['PUT'])
@login_required
@somente_admin()
def atualizar():
    return atualizar_livro()

@livros_blueprint.route('/listar_livros')
@login_required
def listar_livros_json():
    return listar_livros()

@livros_blueprint.route('/livro/<titulo>')
@login_required
def pagina_livro(titulo):
    return listar_um_livro(titulo)
