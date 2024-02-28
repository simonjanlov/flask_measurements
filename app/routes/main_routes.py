from flask import Blueprint, render_template, request
from app.models import db, RecordsModel
from app.utils.graph_generator import generate_graph
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
        try:
            if isinstance(ordered_data, OrderedDict):
                # Store in database
                weight_data = RecordsModel(*list(ordered_data.values()))
                db.session.add(weight_data)
                db.session.commit()
            else:
                raise TypeError("Input must be an OrderedDict")
        except TypeError as te:
            print(f"Error: {te}")
        

        

        # TO DO: Add functionality so that a record is updated by the values in the form that are not empty(0.0)?
        # Decide how to design the functionality overall - should a user only be able to have one weight record each?
          
        # Do something with the ordered data, such as processing the form data
        return 'Form data processed successfully!'
