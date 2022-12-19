from flask import Flask, request
import sqlite3
import jwt
from query_db import *
import datetime
app = Flask(__name__)

# 1. login
# curl -X POST -H "Content-Type: application/json" -d '{"username":"dixin.fan","password":"dixin"}' http://127.0.0.1:5000/login
# {"code":200,"msg":"Password is correct"}
@app.route("/api/login", methods=["POST"])
def login():
    # Retrieve the user data from the request
    params = request.get_json()
    username = params["username"]
    password = params["password"]

    # # Query the database to check if the user exists
    sql = "SELECT * FROM users WHERE name='"+username+"';"
    user = query(sql)

    response = {}
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

        uid, name = user[0], user[1]

        sql = "SELECT * FROM roles WHERE uid="+str(uid)+";"
        role = query(sql)

        # 设置 JWT 令牌的有效时间为 3 分钟
        expiry_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=3)
        
        data = {'uid': uid, 'name': name, 'role': role[2], "exp": expiry_time}
        response['data'] = data

        response['token'] = generate_token(data)
        return response
    else:
        response['msg'] =  "Password is incorrect"
        response['code'] = 401
        return response


def generate_token(data):
    secret = 'secret-key'
    return jwt.encode(data, secret, algorithm='HS256')