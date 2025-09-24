from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Welcome to the Flask REST API!"

# Example GET route
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"message": "No users yet"})

if __name__ == "__main__":
    app.run(debug=True)
