from flask import Blueprint, render_template, request
from app.models import db, RecordsModel
from app.utils.graph_generator import generate_graph, generate_weight_graph, generate_weight_graph_gif
from app.utils.form_data_support import weight_input_transform
from collections import OrderedDict

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
        # Create an ordered dict to hold the form data
        ordered_data = weight_input_transform(request.form)

        # Check ordered_data for correct type
        if not isinstance(ordered_data, OrderedDict):
            error_message = "Error: Input must be an OrderedDict"
            print(error_message)
            return render_template("pages/error.html", message=error_message)

        # Begin a database transaction
        db.session.begin()

        try:
            # Store in database
            weight_data = RecordsModel(*list(ordered_data.values()))
            db.session.add(weight_data)
        except Exception as e:
            print(f"An error occurred: {e}")
            db.session.rollback()
            return render_template("pages/error.html", message=str(e))
        else:
            # Commit the transaction if no exceptions occurred
            db.session.commit()
            generate_weight_graph(list(ordered_data.values()))
            generate_weight_graph_gif(list(ordered_data.values()))


        return render_template("pages/user_graph.html")
