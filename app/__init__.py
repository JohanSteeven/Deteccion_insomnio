from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Registrar las rutas desde routes.py
    from .routes import api
    app.register_blueprint(api)
    
    return app
