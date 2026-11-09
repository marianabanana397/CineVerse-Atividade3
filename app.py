
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cineverse"
    )

@app.route("/catalogo", methods=["GET"])
def listar_catalogo():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, titulo, tipo, genero, ano FROM catalogo"
    )
    registros = cursor.fetchall()

    cursor.close()
    conexao.close()

    return jsonify(registros), 200

@app.route("/catalogo", methods=["POST"])
def cadastrar_catalogo():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado foi enviado"}), 400

    campos = ["titulo", "tipo", "genero", "ano"]

    if any(not dados.get(campo) for campo in campos):
        return jsonify({"erro": "Preencha todos os campos"}), 400

    try:
        ano = int(dados["ano"])
    except (ValueError, TypeError):
        return jsonify({"erro": "O ano deve ser um número"}), 400

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO catalogo (titulo, tipo, genero, ano) VALUES (%s, %s, %s, %s)",
        (dados["titulo"], dados["tipo"], dados["genero"], ano)
    )

    conexao.commit()
    novo_id = cursor.lastrowid

    cursor.close()
    conexao.close()

    return jsonify({
        "mensagem": "Título cadastrado com sucesso!",
        "id": novo_id
    }), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)
