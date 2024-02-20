import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from flask_migrate import Migrate
from dotenv import load_dotenv
from app.routes.main_routes import main_bp
from app.models.records import db, RecordsModel


load_dotenv()

# Application factory
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
        f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Set up database configuration
    db.init_app(app)

    # Initialize flask-migrate
    migrate = Migrate(app, db)
    
    # Test that the database connection works
    try:    
        with app.app_context():
            RecordsModel.query.first()
            print("\nSuccessfully conncted to database")
    except OperationalError as e:
        # Terminate the program if the database connection is faulty
        print(f"\nInvalid database connection settings: {e}")
        sys.exit(1)
    except Exception as e:
        print("Unexpected error (Database connection):", e)
        sys.exit(1)
    
    app.register_blueprint(main_bp)

    return app


app = create_app()
