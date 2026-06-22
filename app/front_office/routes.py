from flask import render_template, redirect, url_for


from app.front_office import front_bp

from . import front_bp

@front_bp.route('/')
def home():
    return redirect(url_for('front_office.login'))

@front_bp.route('/services/', defaults={'id': None})
@front_bp.route('/services/<id>')
def services(id):
    if id != None:
        return "Servicio: " + str(id)
    else:
        services = [{'title': 'Panel de Automatizaciones', 'description': 'Panel de Automatizaciones', 'id': 1},{'title': 'Panel de Automatizaciones', 'description': 'Panel de Automatizaciones', 'id': 2}]
        return render_template('front/index.html', services=services)

@front_bp.route('/login/')
def login():
    return render_template('front/login.html')