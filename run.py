from app.app import create_app, db
import os

app = create_app()

# Comando para crear las tablas
@app.cli.command('create-db')
def create_db():
    print('hola')
    db.create_all()
    print("Tablas creadas correctamente.")


    # Inicializar extensiones
    #migrate.init_app(app, db)}
    
    #migrate = Migrate()

if __name__ == "__main__":
    app.run(debug=True, port=4000)
