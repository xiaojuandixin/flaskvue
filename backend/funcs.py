from flask import Flask, request
import sqlite3
app = Flask(__name__)

# 1. login
# curl -X POST -H "Content-Type: application/json" -d '{"username":"dixin.fan","password":"dixin"}' http://127.0.0.1:5000/login
# {"code":200,"msg":"Password is correct"}
@app.route("/api/login", methods=["POST"])
def login():
    response = {}
    # Retrieve the user data from the request
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    # Query the database to check if the user exists
    conn = sqlite3.connect("pfm.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name=?", (username,))
    user = cursor.fetchone()
    conn.close()

    # If the user doesn't exist, return a 404 error
    if not user:
        response['msg'] =  "User not found"
        response['code'] = 404
        return response

    # If the user exists, check if their password is correct
    db_password = user[2]  # Assume the password is stored in the third column of the user row
    if db_password == password:
        response['msg'] =  "Password is correct"
        response['code'] = 200
        return response
    else:
        response['msg'] =  "Password is incorrect"
        response['code'] = 401
        return response