from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///./site.db')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-please-change')
    
    db.init_app(app)

    
    from routes import register_routes
    register_routes(app, db)


    migrate = Migrate(app, db)

    return app