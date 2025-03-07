from config import conexao, cursor

class Livros:
    def __init__(self, titulo, autor, publicacao, tema):
        self.titulo = titulo
        self.autor = autor
        self.publicacao = publicacao
        self.tema = tema

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