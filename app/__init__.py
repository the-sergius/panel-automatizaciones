from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Registrar los Blueprints
    from app.front_office import front_bp
    #from app.back_office import back_bp

    from app.front_office import routes as front_routes

    app.register_blueprint(front_bp, url_prefix='/')
    #app.register_blueprint(back_bp, url_prefix='/admin')
    
    return app