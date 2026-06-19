from flask import Blueprint

front_bp = Blueprint('front_office', __name__)









# from flask import Flask, render_template, jsonify, request, url_for, redirect

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('front/index.html')

# @app.route("/services")
# def services():
#     services=[{
#         "title": "Panel de Automatizaciones",
#         "description": "Panel de Automatizaciones",
#         "id": 1
#         },
#         {
#         "title": "Panel de Automatizaciones",
#         "description": "Panel de Automatizaciones",
#         "id": 2
#         }]
#     return render_template('front/services.html', services=services)

# @app.route('/login', methods=['POST'])
# def login():
#     if request.form['password'] != '':
#         return jsonify({'message': 'Invalid credentials'}), 401
#     else:
#         return redirect(url_for('services'))

# if __name__ == '__main__':
#     app.run(debug=True)