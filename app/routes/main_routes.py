from flask import Blueprint, render_template
from app.utils.graph_generator import generate_graph

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    generate_graph()
    return render_template("pages/home.html")

@main_bp.route("/about")
def about():
    return render_template("pages/about.html")

@main_bp.route("/submit_weight")
def submit_weight():
    return render_template("pages/submit_weight.html")