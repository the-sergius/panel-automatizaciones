from flask import render_template


from app.back_office import back_bp

from . import back_bp

@back_bp.route('/admin')
def home():
    return render_template('back/index.html')