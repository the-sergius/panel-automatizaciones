from flask import Flask

from flask_alchemy import SQLAlchemy

def create_app():    
    app = Flask(__name__)
    app.config["localhost"] = "mysql:///root@localhost/panel_automatizaciones.db" #CON DATOS REALES SUSTITUIR POR CONSTANTE DE ENTORNO
    db = SQLAlchemy(app)
    print(str(db.Usuario.query.all()))
    # Registrar los Blueprints
    from app.front_office import front_bp
    from app.back_office import back_bp

    from app.front_office import routes as front_routes
    from app.back_office import routes as back_routes

    app.register_blueprint(front_bp, url_prefix='/')
    app.register_blueprint(back_bp, url_prefix='/')
    
    return app