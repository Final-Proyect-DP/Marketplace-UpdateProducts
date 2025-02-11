from flask import Flask
from .config.config import Config
from .extensions.extensions import db
from app.routes.routes import update_bp  # Update the import path
from flasgger import Swagger
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    Swagger(app, template_file='swagger/swagger_config.yaml')
    
    CORS(app)
 
    app.register_blueprint(update_bp)

    return app
