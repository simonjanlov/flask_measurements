from flask import Flask
from dotenv import load_dotenv
import os
from app.routes.main_routes import main_bp


load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
        f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    )
    
    # print(app.config['SQLALCHEMY_DATABASE_URI'])


    app.register_blueprint(main_bp)
    
    return app

