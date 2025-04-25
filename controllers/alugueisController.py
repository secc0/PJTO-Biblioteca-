from flask import request, jsonify, session, redirect, url_for
from models.alugueis import Alugueis
from config import conexao, cursor
from datetime import datetime
from config import conectar_bd
import traceback
from mysql.connector import errors

def alugar_livro():
    try:
        # [1] Verificações iniciais
        if 'user' not in session:
            return "Usuário não autenticado.", 401
            
        titulo_livro = request.form.get('titulo', '').strip()
        if not titulo_livro:
            return "Título do livro é obrigatório.", 400

        # [2] Conexão com o banco
        conexao = conectar_bd()
        if not conexao:
            return "Erro ao conectar no banco.", 500

        try:
            # [3] Consulta ÚNICA com JOIN para evitar múltiplas queries
            query = """
                SELECT l.id, 
                       COUNT(a.id) > 0 as ja_alugado
                FROM livros l
                LEFT JOIN alugueis a ON a.livro_id = l.id AND a.devolvido = FALSE
                WHERE l.titulo = %s
                GROUP BY l.id
                LIMIT 1
            """
            
            with conexao.cursor() as cursor:
                cursor.execute(query, (titulo_livro,))
                resultado = cursor.fetchone()
                
                if not resultado:
                    return "Livro não encontrado.", 404
                    
                livro_id, ja_alugado = resultado
                
                if ja_alugado:
                    return "Este livro já está alugado.", 409
                
                # [4] Registro do aluguel
                cursor.execute("""
                    INSERT INTO alugueis 
                    (usuario_id, livro_id, data_aluguel, devolvido)
                    VALUES (%s, %s, NOW(), FALSE)
                """, (session['user']['id'], livro_id))
                
                conexao.commit()
                return redirect(url_for("front.listar"))

        except Exception as e:
            conexao.rollback()
            print(f"Erro: {str(e)}")
            return f"Erro ao processar aluguel: {str(e)}", 500
            
        finally:
            conexao.close()

    except Exception as e:
        print(f"Erro geral: {str(e)}")
        return "Erro interno no sistema.", 500







def devolver_livro(aluguel_id):
    try:
        resposta, status = Alugueis.devolver(aluguel_id)
        return jsonify(resposta), status
    except Exception as e:
        return jsonify({"erro": f"Erro ao processar devolução: {str(e)}"}), 400

def listar_alugueis():
    try:
        alugueis = Alugueis.listar()
        return jsonify(alugueis)
    except Exception as e:
        return jsonify({"erro": f"Erro ao listar aluguéis: {str(e)}"}), 400
