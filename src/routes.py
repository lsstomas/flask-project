from flask import render_template, request, redirect, url_for
from .models import Produto


def init_routes(app):

    # Rota principal da aplicação (listagem de produtos)
    @app.route("/")
    def index():
        produtos = Produto.get_all()
        return render_template("index.html", produtos=produtos)

    # Rota para adicionar um produto
    @app.route("/add", methods=["GET", "POST"])
    def add_product():
        if request.method == "POST":
            nome = request.form["nome"]
            descricao = request.form["descricao"]
            preco = request.form["preco"]
            novo_produto = Produto(nome, descricao, preco)
            novo_produto.save_to_db()
            return redirect(url_for("index"))
        
        return render_template("add_product.html")

    @app.route("/edit/<int:product_id>", methods=["GET", "POST"])
    def edit_product(product_id):
        produto = Produto.get(product_id)
        if request.method == "POST":
            produto.nome = request.form["nome"]
            produto.descricao = request.form["descricao"]
            produto.preco = request.form["preco"]
            produto.update_in_db()
            return redirect(url_for("index"))
        return render_template("edit_product.html", produto=produto)

    @app.route("/delete/<int:product_id>")
    def delete_product(product_id):
        Produto.delete_from_db(product_id)
        return redirect(url_for("index"))
