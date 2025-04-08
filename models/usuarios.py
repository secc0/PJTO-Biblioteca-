from config import conexao, cursor
import mysql.connector

class Usuarios:
    def __init__(self, nome, telefone, email, senha, perfil):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.perfil = perfil

    def salvar(self):
        try:
            if conexao.is_connected():
                sql_verificar = "SELECT id FROM usuarios WHERE email = %s"
                cursor.execute(sql_verificar, (self.email,))
                resultado = cursor.fetchone()

                if resultado:
                    return {"erro": f"E-mail '{self.email}' já está cadastrado."}, 400
                else:
                    sql_inserir = "INSERT INTO usuarios (nome, telefone, email, senha, perfil) VALUES (%s, %s, %s, %s, %s)"
                    valores = (self.nome, self.telefone, self.email, self.senha, self.perfil)
                    cursor.execute(sql_inserir, valores)
                    conexao.commit()
                    return({"sucesso": f"Usuário '{self.nome}' adicionado com sucesso!"}), 200
            else:
                print("Erro: Conexão com o banco não está ativa.")
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")

    def deletar(email):
        try:
            if conexao.is_connected():
                cursor = conexao.cursor()
                sql_verificar = "SELECT id FROM usuarios WHERE email = %s"
                cursor.execute(sql_verificar, (email,))
                resultado = cursor.fetchone()

                if resultado:
                    sql = "DELETE FROM usuarios WHERE email = %s"
                    cursor.execute(sql, (email,))
                    conexao.commit()
                    return {"sucesso": "Usuário excluído com sucesso"}, 200
                else:
                    return {"erro": "Usuário não encontrado"}, 404
            else:
                return {"erro": "Erro na conexão com o banco de dados"}, 500

        except Exception as e:
            return {"erro": f"Erro ao excluir usuário: {str(e)}"}, 400

    @staticmethod
    def atualizar(nome, telefone, email, senha, perfil):
        try:
            if conexao.is_connected():
                print("opa")
                sql = """UPDATE usuarios 
                        SET telefone = %s, email = %s, senha = %s, perfil = %s
                        WHERE nome = %s"""
                cursor = conexao.cursor()
                cursor.execute(sql, (telefone, email, senha, perfil, nome))
                conexao.commit()
                print(f"Usuário '{nome}' atualizado com sucesso!")
            else:
                print("Erro: Conexão com o banco não está ativa.")
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")


    @staticmethod
    def autenticar(email, senha):
        try:
            cursor = conexao.cursor()
            sql = "SELECT perfil FROM usuarios WHERE email = %s AND senha = %s"
            cursor.execute(sql, (email, senha))
            return cursor.fetchone()
        except Exception as e:
            print("Erro na autenticação:", e)
            return None