# 🧑‍💻 User Management REST API (Flask)

This is a simple RESTful API built with **Flask** in Python to manage user data. It supports basic CRUD operations and stores data in memory or in a JSON file.

## 🚀 Features
- Get all users
- Get user by ID
- Create new user
- Update existing user
- Delete user
## 🛠️ Tech Stack
- Python 3.10+
- Flask
- cURL or Postman (for testing)
- JSON (for optional persistent storage)
- 
## 📂 Project Structure
project-root/
├── main.py # Flask application
├── users.json # Optional (used for JSON-based persistence)
└── README.md # Project documentation

# Create a user
curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d "{\"id\": 1, \"name\": \"Alice\", \"email\": \"alice@example.com\"}"

# Get all users
curl http://127.0.0.1:5000/users

# Get user by ID
curl http://127.0.0.1:5000/users/1

# Update user
curl -X PUT http://127.0.0.1:5000/users/1 -H "Content-Type: application/json" -d "{\"name\": \"Alice Updated\"}"

# Delete user
curl -X DELETE http://127.0.0.1:5000/users/1
