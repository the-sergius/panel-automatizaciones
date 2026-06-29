from flask import render_template

from app.back_office import back_bp

from . import back_bp

@back_bp.route('/admin')
def home():
    existeAdmin = True
    if not existeAdmin:
        return redirect(url_for('back_office.login'))
    else:
        return render_template('back/index.html')

@back_bp.route('/register')
def register():
    return render_template('back/register.html')