from app import create_app, db
# Importa los modelos

app = create_app()

# Comando para crear las tablas
@app.cli.command('create-db')
def create_db():
    """Crear tablas en la base de datos."""
    db.create_all()
    print("Tablas creadas correctamente.")


if __name__ == "__main__":
    app.run(debug=True, port=4000)
