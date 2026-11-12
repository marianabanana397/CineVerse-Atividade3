
from flask import Flask, request, jsonify
from flask_cors import CORS
from catalogo import Catalogo
from catalogo_dao import CatalogoDAO

app = Flask(__name__)
CORS(app)

dao = CatalogoDAO()


@app.route("/catalogo", methods=["GET"])
def listar_catalogo():
    try:
        registros = dao.listar_todos()

        resultado = []
        for item in registros:
            resultado.append(item.to_dict())

        return jsonify(resultado), 200

    except Exception as erro:
        return jsonify({"erro": str(erro)}), 500


@app.route("/catalogo", methods=["POST"])
def cadastrar_catalogo():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado foi enviado"}), 400

    campos = ["titulo", "tipo", "genero", "ano"]

    if any(
        campo not in dados or dados[campo] is None
        or str(dados[campo]).strip() == ""
        for campo in campos
    ):
        return jsonify({"erro": "Preencha todos os campos"}), 400

    try:
        ano = int(dados["ano"])

        item = Catalogo(
            dados["titulo"],
            dados["tipo"],
            dados["genero"],
            ano
        )

        novo_item = dao.cadastrar(item)

        return jsonify({
            "mensagem": "Título cadastrado com sucesso!",
            "catalogo": novo_item.to_dict()
        }), 201

    except (ValueError, TypeError):
        return jsonify({"erro": "O ano deve ser um número"}), 400

    except Exception as erro:
        return jsonify({"erro": str(erro)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
