from app import create_app

# Creamos la instancia de la aplicación Flask
app = create_app()

if __name__ == '__main__':
    # Arranca el servidor local de desarrollo
    app.run(debug=True)