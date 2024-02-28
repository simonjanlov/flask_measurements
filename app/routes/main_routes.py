from flask import Blueprint, render_template, request
from app.models import db, RecordsModel
from app.utils.graph_generator import generate_graph
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
        ordered_data = OrderedDict()

        # As long as the data can be converted to type float, add to ordered_data
        try:
            for key, value in request.form.items():
                if key != 'week_10':
                    # Allow empty input
                    if value == "":
                        ordered_data[key] = 0.0
                    else:
                        ordered_data[key] = float(value)
            # Add "week_10" at the end of ordered_data (to ensure that week_10 comes at the end and not between week_1 and week_2)
            if 'week_10' in request.form:
                # Allow empty input
                    if value == "":
                        ordered_data['week_10'] = 0.0
                    else:
                        ordered_data['week_10'] = float(request.form['week_10'])
        except ValueError as e:
            return "Invalid input"

        # Store in database
        weight_data = RecordsModel(*list(ordered_data.values()))
        db.session.add(weight_data)
        db.session.commit()

        # TO DO: Add functionality so that a record is updated by the values in the form that are not empty(0.0)?
        # Decide how to design the functionality overall - should a user only be able to have one weight record each?
          
        # Do something with the ordered data, such as processing the form data
        return 'Form data processed successfully!'
