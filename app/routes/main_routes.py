from flask import Blueprint, render_template, request
from app.models.records import RecordsModel
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
        # Create an ordered dict and convert values into floats
        ordered_data = OrderedDict()

        try:
            # Move all items except "week_10" to the ordered_data
            for key, value in request.form.items():
                if key != 'week_10':
                    ordered_data[key] = float(value)
            # Add "week_10" at the end of ordered_data
            if 'week_10' in request.form:
                ordered_data['week_10'] = float(request.form['week_10'])
        except ValueError as e:
            return "Invalid input"

        # Create an OrderedDict to preserve the order of insertion
        # ordered_data = OrderedDict()
        # # Move all items except "week_10" to the ordered_data
        # for key, value in request.form.items():
        #     if key != 'week_10':
        #         ordered_data[key] = value
        # # Add "week_10" at the end of ordered_data
        # if 'week_10' in request.form:
        #     ordered_data['week_10'] = request.form['week_10']

        # # Print the ordered data for verification
        # for key, value in ordered_data.items():
        #     print(f"{key}: {value}")

        # # Store in database
        weight_data = RecordsModel(*list(ordered_data.values()))
        print(weight_data)
            
        # Do something with the ordered data, such as processing the form data
        return 'Form data processed successfully!'
