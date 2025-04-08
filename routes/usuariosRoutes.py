from flask import Blueprint, request, jsonify, redirect, url_for
from controllers.usuariosController import (
    adicionar_usuario,
    excluir_usuario,
    atualizar_usuario,
    processar_login
)
from decorators.autenticacao import  somente_admin

usuarios_blueprint = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@usuarios_blueprint.route('/adicionar_usuario', methods=['POST'])
def adicionar():
    return adicionar_usuario()

@usuarios_blueprint.route('/deletar_usuario', methods=['DELETE'])
@somente_admin()
def excluir():
    return excluir_usuario()

@usuarios_blueprint.route('/atualizar_usuario', methods=['PUT'])
def atualizar():
    return atualizar_usuario()

@usuarios_blueprint.route("/login", methods=["POST"])
def logar():
    return processar_login()
