from flask import render_template, redirect, url_for


from app.front_office import front_bp

from . import front_bp

@front_bp.route('/')
def home():
    services = [{},{}]
    return render_template('front/index.html', services=services)
    return redirect(url_for('front_office.login'))

@front_bp.route('/login')
def login():
    return render_template('front/index.html')