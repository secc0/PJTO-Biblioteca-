from flask import request, jsonify, redirect, url_for, make_response, render_template
from models.usuarios import Usuarios

def adicionar_usuario():
    try:
        dados = request.json
        usuario = Usuarios(
            nome=dados["nome"],
            telefone=dados["telefone"],
            email=dados["email"],
            senha=dados["senha"],
            perfil=dados["perfil"]
        )

        resposta, status = usuario.salvar()
        return jsonify(resposta), status

    except Exception as e:
        return f"Erro ao criar usuário: {str(e)}", 400
    
def excluir_usuario():
    try:
        dados = request.json
        email = dados["email"]
        
        resposta, status = Usuarios.deletar(email)
        return jsonify(resposta), status

    except Exception as e:
        return jsonify({"erro": f"Erro ao deletar usuário: {str(e)}"}), 400

def atualizar_usuario():
    try:
        dados = request.json

        nome = dados["nome"]
        telefone = dados.get("telefone")
        email = dados.get("email")
        senha = dados.get("senha")
        perfil = dados.get("perfil")

        Usuarios.atualizar(nome, telefone, email, senha, perfil)
        return jsonify({"mensagem": "Usuário atualizado com sucesso!"}), 200

    except Exception as e:
        return jsonify({"erro": f"Erro ao atualizar usuário: {str(e)}"}), 400

def processar_login():
    try:
        dados = request.form
        email = dados.get("email")
        senha = dados.get("senha")

        if not email or not senha:
            return render_template("login.html", erro="Preencha todos os campos.")

        if Usuarios.autenticar(email, senha):
            resposta = make_response(redirect(url_for("livros.listar")))
            resposta.set_cookie("email", email)
            return resposta
        else:
            return render_template("login.html", erro="Usuário ou senha incorretos.")
    except Exception as e:
        return render_template("login.html", erro=f"Erro no login: {str(e)}")