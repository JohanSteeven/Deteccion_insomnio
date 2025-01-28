from app import create_app

app = create_app()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Usar el puerto de Railway
    print(f"🚀 Aplicación ejecutándose en el puerto {port}")
    app.run(host="0.0.0.0", port=port)
