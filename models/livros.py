from config import conexao, cursor
import mysql.connector

class Livros:
    def __init__(self, titulo, autor, publicacao, tema, imagem):
        self.titulo = titulo
        self.autor = autor
        self.publicacao = publicacao
        self.tema = tema
        self.imagem = imagem

    @staticmethod
    def criar_tabela():
        try:
            if conexao.is_connected():
                # Comando SQL para criar a tabela 'livros' se ela não existir
                sql = """
                CREATE TABLE IF NOT EXISTS livros (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    titulo VARCHAR(255) NOT NULL,
                    autor VARCHAR(255) NOT NULL,
                    publicacao DATE NOT NULL,
                    tema VARCHAR(255) NOT NULL,
                    imagem VARCHAR(255) NOT NULL
                );
                """
                cursor.execute(sql)
                conexao.commit()
                print("Tabela 'livros' criada com sucesso!")
            else:
                print("Erro: Conexão com o banco não está ativa.")
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")

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

    def atualizar(self, titulo, atualizar, autor, publicacao, tema, imagem):
        try:
            if conexao.is_connected():
                sql = """UPDATE LIVROS;
                  SET titulo = %s, autor = %s, publicacao = %s, tema = %s, imagem = %s;
                    WHERE titulo = %s"""
                cursor = conexao.cursor()
                cursor.execute(sql, (atualizar, autor, publicacao, tema, imagem, titulo))
                conexao.commit()
                print(f"Livro atualizado com sucesso")
            else:
                print("aqui deu ruim.")
        except Exception as e:
            print(f"Erro ao inserir livro: {e}")        

@staticmethod
def buscar_todos():
    try:
        if conexao.is_connected():
            cursor.execute("SELECT * FROM livros")
            livros = cursor.fetchall()
            # tupla p dic
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