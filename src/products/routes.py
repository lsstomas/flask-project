from flask import Blueprint, render_template, request

bp_produto = Blueprint("produto", __name__, template_folder="templates")


@bp_produto.route("/")
def index():
    return render_template("index.html")


@bp_produto.route("/adicionar", methods=["GET", "POST"])
def create_product():
    if request.method == "POST":
        nome = request.form.get["nome"]
        descricao = request.form.get["descricao"]
        preco = request.form.get["preco"]

        return f"Nome: {nome} | Descricão: {descricao} | Preço: {preco}"

    return render_template("add_product.html")
