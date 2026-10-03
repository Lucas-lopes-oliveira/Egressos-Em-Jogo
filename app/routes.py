from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("index.html"), 404