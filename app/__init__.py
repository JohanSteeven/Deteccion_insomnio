import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registrar las rutas desde routes.py
    from .routes import api
    app.register_blueprint(api)

    return app

# Iniciar la aplicación correctamente si este archivo es el punto de entrada
if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5000))  # Obtener el puerto de Railway
    print(f"🚀 Iniciando aplicación en el puerto {port}")
    app.run(host="0.0.0.0", port=port)
