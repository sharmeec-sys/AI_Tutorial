from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    return jsonify({
        "operation": "addition",
        "result": a + b
    })

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    return jsonify({
        "operation": "subtraction",
        "result": a - b
    })

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    return jsonify({
        "operation": "multiplication",
        "result": a * b
    })

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')

    if b == 0:
        return jsonify({"error": "Division by zero not allowed"}), 400

    return jsonify({
        "operation": "division",
        "result": a / b
    })

if __name__ == '__main__':
    app.run(debug=True)
