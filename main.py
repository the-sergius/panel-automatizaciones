from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] != '':
        return jsonify({'message': 'Invalid credentials'}), 401
    else:
        return jsonify({'message': 'Login successful!'}), 200

if __name__ == '__main__':
    app.run(debug=True)