
import mysql.connector
from catalogo import Catalogo


class CatalogoDAO:

    def conectar(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cineverse"
        )

    def listar_todos(self):
        conexao = self.conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute(
            "SELECT id, titulo, tipo, genero, ano FROM catalogo"
        )

        registros = cursor.fetchall()

        cursor.close()
        conexao.close()

        catalogo = []

        for registro in registros:
            item = Catalogo(
                registro["titulo"],
                registro["tipo"],
                registro["genero"],
                registro["ano"],
                registro["id"]
            )
            catalogo.append(item)

        return catalogo

    def cadastrar(self, item):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """INSERT INTO catalogo
            (titulo, tipo, genero, ano)
            VALUES (%s, %s, %s, %s)""",
            (item.titulo, item.tipo, item.genero, item.ano)
        )

        conexao.commit()
        item.id = cursor.lastrowid

        cursor.close()
        conexao.close()

        return item
