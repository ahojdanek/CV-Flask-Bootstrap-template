from flask import Flask, render_template, Blueprint

products_bp = Blueprint('products_bp', __name__,
                       template_folder='templates',
                       static_folder='static')


@products_bp.route("/detail")
def home():
    return render_template("/detail.html")