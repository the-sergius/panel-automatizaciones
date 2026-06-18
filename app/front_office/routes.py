from flask import Blueprint, render_template


from app.front_office import front_bp
#front_bp = Blueprint('front_office', __name__)

from . import front_bp

@front_bp.route('/')
def home():
    return render_template('front/index.html')