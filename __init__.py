from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask( __name__ , instance_relative_config=False)
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Quark@2416@localhost:3306/test'
    db = SQLAlchemy(app)
    
    
    with app.app_context():
        db.create_all()
        return app