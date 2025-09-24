# 🚀 Flask REST API

A simple REST API built with **Flask** that manages user data.  
This project was created as part of a Python Developer Internship task.

---

## 📌 Features
- Create users (`POST /users`)
- Retrieve all users (`GET /users`)
- Update a user (`PUT /users/<id>`)
- Delete a user (`DELETE /users/<id>`)
- In-memory storage using Python dictionary

---

## 🛠️ Tech Stack
- **Python 3**
- **Flask**
- **Postman / Curl** (for testing)

---

## 📂 Project Structure
broskieshub/
│
├── flask_rest_api.py # Main Flask app
└── README.md # Documentation

yaml
Copy code

---

## ⚡ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/flask-rest-api.git
cd flask-rest-api
2️⃣ Create Virtual Environment (Optional but Recommended)
bash
Copy code
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux
3️⃣ Install Dependencies
bash
Copy code
pip install flask
4️⃣ Run the App
bash
Copy code
python flask_rest_api.py
By default, it runs at 👉 http://127.0.0.1:5000

🔗 API Endpoints
Method	Endpoint	Description
GET	/users	Get all users
POST	/users	Add a new user
PUT	/users/<id>	Update a user
DELETE	/users/<id>	Delete a user

🧪 Testing the API
Using Postman or Curl
GET Users

bash
Copy code
curl http://127.0.0.1:5000/users
POST User

bash
Copy code
curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "email": "john@example.com"}'
PUT User

bash
Copy code
curl -X PUT http://127.0.0.1:5000/users/1 \
-H "Content-Type: application/json" \
-d '{"name": "Jane Doe", "email": "jane@example.com"}'
DELETE User

bash
Copy code
curl -X DELETE http://127.0.0.1:5000/users/1
