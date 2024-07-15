from flask import Flask, jsonify

app = Flask(__name__)

users = {
    1: {"name": "John Doe", "email": "john@example.com"},
    2: {"name": "Jane Doe", "email": "jane@example.com"}
}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
