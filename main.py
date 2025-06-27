from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
FILE = 'users.json'

# Load users from file or initialize empty dict
def load_users():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return {}

# Save users to file
def save_users(users):
    with open(FILE, 'w') as f:
        json.dump(users, f, indent=2)

@app.route('/users', methods=['GET'])
def get_users():
    users = load_users()
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = load_users()
    user = users.get(str(user_id))
    if user:
        return jsonify({user_id: user})
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    users = load_users()
    user_id = str(data['id'])
    if user_id in users:
        return jsonify({'error': 'User already exists'}), 409
    users[user_id] = {'name': data['name'], 'email': data['email']}
    save_users(users)
    return jsonify({'message': 'User created'}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    users = load_users()
    user_id = str(user_id)
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    users[user_id].update(data)
    save_users(users)
    return jsonify({'message': 'User updated'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = load_users()
    user_id = str(user_id)
    if user_id in users:
        del users[user_id]
        save_users(users)
        return jsonify({'message': 'User deleted'})
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
