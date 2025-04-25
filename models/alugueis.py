from config import conexao, cursor
from datetime import datetime

class Alugueis:
    def __init__(self, usuario_id, livro_id):
        self.usuario_id = usuario_id
        self.livro_id = livro_id

    def alugar(self):
        try:
            if conexao.is_connected():
                sql = """
                    INSERT INTO alugueis (usuario_id, livro_id, data_aluguel, devolvido)
                    VALUES (%s, %s, %s, %s)
                """
                valores = (self.usuario_id, self.livro_id, datetime.now(), False)
                cursor.execute(sql, valores)
                conexao.commit()
                return {"sucesso": "Livro alugado com sucesso!"}, 201
            else:
                return {"erro": "Sem conexão com o banco"}, 500
        except Exception as e:
            return {"erro": f"Erro ao alugar livro: {e}"}, 400

    @staticmethod
    def devolver(aluguel_id):
        try:
            if conexao.is_connected():
                sql = """
                    UPDATE alugueis
                    SET devolvido = TRUE, data_devolucao = %s
                    WHERE id = %s AND devolvido = FALSE
                """
                valores = (datetime.now(), aluguel_id)
                cursor.execute(sql, valores)
                conexao.commit()
                if cursor.rowcount > 0:
                    return {"sucesso": "Livro devolvido com sucesso!"}, 200
                else:
                    return {"erro": "Aluguel não encontrado ou já devolvido."}, 404
            else:
                return {"erro": "Sem conexão com o banco"}, 500
        except Exception as e:
            return {"erro": f"Erro ao devolver livro: {e}"}, 400

    @staticmethod
    def listar():
        try:
            if conexao.is_connected():
                sql = """
                    SELECT a.id, u.nome, l.titulo, a.data_aluguel, a.data_devolucao, a.devolvido
                    FROM alugueis a
                    JOIN usuarios u ON a.usuario_id = u.id
                    JOIN livros l ON a.livro_id = l.id
                """
                cursor.execute(sql)
                registros = cursor.fetchall()
                alugueis = [{
                    "id": r[0],
                    "usuario": r[1],
                    "livro": r[2],
                    "data_aluguel": r[3],
                    "data_devolucao": r[4],
                    "devolvido": r[5]
                } for r in registros]
                return alugueis
            else:
                return []
        except Exception as e:
            print(f"Erro ao listar aluguéis: {e}")
            return []
