from config import conexao, cursor

class Livros:
    def __init__(self, titulo, autor, publicacao, tema,):
        self.titulo = titulo
        self.autor = autor
        self.publicacao = publicacao
        self.tema = tema

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
                    tema VARCHAR(255) NOT NULL
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
                sql = "INSERT INTO livros (titulo, autor, publicacao, tema) VALUES (%s, %s, %s, %s)"
                valores = (self.titulo, self.autor, self.publicacao, self.tema)
                cursor.execute(sql, valores)
                conexao.commit()
                print(f"Livro '{self.titulo}' adicionado com sucesso!")
            else:
                print("Erro: Conexão com o banco não está ativa.")
        except Exception as e:
            print(f"Erro ao inserir livro: {e}")

    @staticmethod
    def buscar_todos():
        try:
            if conexao.is_connected():
                cursor.execute("SELECT * FROM livros")
                livros = cursor.fetchall()
                return livros
            else:
                print("Erro: Conexão com o banco não está ativa.")
                return []
        except Exception as e:
            print(f"Erro ao buscar livros: {e}")
            return []