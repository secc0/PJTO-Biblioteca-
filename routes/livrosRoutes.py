from flask import Blueprint, request, jsonify, redirect, url_for
from controllers.livrosController import (
    homeLivros,
    adicionar_livro,
    deletar_livro,
    atualizar_livro,
    listar_livros
)
from decorators.autenticacao import login_usuario, somente_admin

livros_blueprint = Blueprint('livros', __name__, url_prefix='/livros')


@livros_blueprint.route('/', methods=['GET'])
@login_usuario()
def home():
    return homeLivros()

@livros_blueprint.route('/adicionar_livro', methods=['POST'])
@somente_admin()
def adicionar():
    return adicionar_livro()

@livros_blueprint.route('/deletar_livro', methods=['DELETE'])
@somente_admin()
def deletar():
    return deletar_livro()

@livros_blueprint.route('/atualizar_livro', methods=['PUT'])
@somente_admin()
def atualizar():
    return atualizar_livro()

@livros_blueprint.route('/listar_livros')
@login_usuario()
def listar():
    return listar_livros()
