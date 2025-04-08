from config import conexao, cursor
import mysql.connector

class Livros:
    def __init__(self, titulo, autor, publicacao, tema, imagem):
        self.titulo = titulo
        self.autor = autor
        self.publicacao = publicacao
        self.tema = tema
        self.imagem = imagem

    def salvar(self):
        try:
            if conexao.is_connected():
                sql = "INSERT INTO livros (titulo, autor, publicacao, tema, imagem) VALUES (%s, %s, %s, %s, %s)"
                valores = (self.titulo, self.autor, self.publicacao, self.tema, self.imagem)
                cursor.execute(sql, valores)
                conexao.commit()
                print(f"Livro '{self.titulo}' adicionado com sucesso!")
            else:
                print("Erro: Conexão com o banco não está ativa.")
        except Exception as e:
            print(f"Erro ao inserir livro: {e}")

    def deletar(self, titulo):
        try:
            if conexao.is_connected():
                sql = "DELETE FROM LIVROS WHERE titulo = %s"
                cursor = conexao.cursor()
                cursor.execute(sql, (titulo,))
                conexao.commit()
                print(f"Livro excluido com sucesso")
            else:
                print("aqui deu ruim.")
        except Exception as e:
            print(f"Erro ao inserir livro: {e}")    

    @staticmethod
    def atualizar(titulo, atualizar, autor, publicacao, tema, imagem):
        try:
            if conexao.is_connected():
                print("opa")
                sql = """UPDATE livros 
                         SET titulo = %s, autor = %s, publicacao = %s, tema = %s, imagem = %s 
                         WHERE titulo = %s"""
                cursor = conexao.cursor()
                cursor.execute(sql, (atualizar, autor, publicacao, tema, imagem, titulo))
                conexao.commit()
                print(f"Livro '{titulo}' atualizado com sucesso!")
            else:
                print("Erro: Conexão com o banco não está ativa.")
        except Exception as e:
            print(f"Erro ao atualizar livro: {e}")      

    @staticmethod
    def buscar_todos():
        try:
            if conexao.is_connected():
                cursor.execute("SELECT * FROM livros")
                livros = cursor.fetchall()
                livros_list = [
                    {
                        'id': livro[0],
                        'titulo': livro[1],
                        'autor': livro[2],
                        'publicacao': livro[3],
                        'tema': livro[4],
                        'imagem': livro[5]
                    } for livro in livros
                ]
                return livros_list
            else:
                print("Erro: Conexão com o banco não está ativa.")
                return []
        except mysql.connector.Error as err:
            print(f"Erro ao buscar livros: {err}")
            return []
        except Exception as e:
            print(f"Erro inesperado ao buscar livros: {e}")
            return []
