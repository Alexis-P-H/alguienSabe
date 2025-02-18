from app.app import create_app, db
import os

app = create_app()

# Comando para crear las tablas
@app.cli.command('create-db')
def create_db():
    #db.create_all()
    # Inicializar extensiones
    #migrate.init_app(app, db)}
    #migrate = Migrate()
    pass

if __name__ == "__main__":
    app.run(debug=True, port=4000)
