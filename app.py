from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/services")
def services():
    services=[{
        "title": "Panel de Automatizaciones",
        "description": "Panel de Automatizaciones",
        "id": 1
        },
        {
        "title": "Panel de Automatizaciones",
        "description": "Panel de Automatizaciones",
        "id": 2
        }]
    return render_template('services.html', servicios=services)

@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] != '':
        return jsonify({'message': 'Invalid credentials'}), 401
    else:
        return jsonify({'message': 'Login successful!'}), 200

if __name__ == '__main__':
    app.run(debug=True)