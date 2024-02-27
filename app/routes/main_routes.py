from flask import Blueprint, render_template, request
from app.utils.graph_generator import generate_graph

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    generate_graph()
    return render_template("pages/home.html")

@main_bp.route("/about")
def about():
    return render_template("pages/about.html")

@main_bp.route("/weight_form", methods = ['POST', 'GET'])
def weight_form():
    if request.method == 'GET':
        return render_template("pages/weight_form.html")
     
    if request.method == 'POST':
        data = request.form
        return data

