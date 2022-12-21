from flask import Flask, request
import sqlite3
import jwt
from query_db import *
import datetime
app = Flask(__name__)

# 1. login
# request
'''
{
  "username": "dixin.fan",
  "password": "dixin"
}
'''
# response
'''
{
  "code": 200,
  "data": {
    "exp": "Mon, 19 Dec 2022 12:56:26 GMT",
    "name": "dixin.fan",
    "role": "sale",
    "uid": 3
  },
  "msg": "Password is correct",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjMsIm5hbWUiOiJkaXhpbi5mYW4iLCJyb2xlIjoic2FsZSIsImV4cCI6MTY3MTQ1NDU4Nn0.6xC7p5Jvr8EaEUrUASoIW8p6C1eVBbXDUy83LiZC6bs"
}
'''
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
        response['msg'] =  "用户不存在"
        response['code'] = 404
        return response

    # If the user exists, check if their password is correct
    db_password = user[2]  # Assume the password is stored in the third column of the user row
    if db_password == password:
        response['msg'] =  "密码正确"
        response['code'] = 200

        uid, name, email= user[0], user[1], user[3]

        sql = "SELECT * FROM roles WHERE uid="+str(uid)+";"
        role = query(sql)

        # 设置 JWT 令牌的有效时间为 3 分钟
        expiry_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=3)
        
        data = {'uid': uid, 'name': name, 'role': role[2], 'email': email, "exp": expiry_time}
        response['data'] = data

        response['token'] = generate_token(data)
        return response
    else:
        response['msg'] =  "密码错误"
        response['code'] = 401
        return response


def generate_token(data):
    secret = 'secret-key'
    return jwt.encode(data, secret, algorithm='HS256')


# 2. editInfo
# request
'''
{
  "username": "dixin.fan",
  "password": "dixin"
}
'''
# response
'''
{
  "code": 200,
  "data": {
    "exp": "Mon, 19 Dec 2022 12:56:26 GMT",
    "name": "dixin.fan",
    "role": "sale",
    "uid": 3
  },
  "msg": "Password is correct",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjMsIm5hbWUiOiJkaXhpbi5mYW4iLCJyb2xlIjoic2FsZSIsImV4cCI6MTY3MTQ1NDU4Nn0.6xC7p5Jvr8EaEUrUASoIW8p6C1eVBbXDUy83LiZC6bs"
}
'''
@app.route("/api/editInfo", methods=["POST"])
def editInfo():
    # Retrieve the user data from the request
    params = request.get_json()
    uid = int(params["uid"])
    email = params["email"]
    pwd = params["pwd"]
    token = params["token"]



    if pwd == "":
      sql = "UPDATE users SET email = '" +email+"' WHERE uid = "+uid;
    else:
      sql = "UPDATE users SET email = '" +email+"', pwd = '"+pwd+"' WHERE uid = "+uid;

    response = {}
    response['msg'] =  "用户不存在"
    response['code'] = 404
    try:
      result = execute_sql(sql)
    except:
      response['msg'] =  "用户不存在"
      response['code'] = 404


    response = {}
    # If the user doesn't exist, return a 404 error
    if not user:
        response['msg'] =  "用户不存在"
        response['code'] = 404
        return response

    # If the user exists, check if their password is correct
    db_password = user[2]  # Assume the password is stored in the third column of the user row
    if db_password == password:
        response['msg'] =  "密码正确"
        response['code'] = 200

        uid, name, email= user[0], user[1], user[3]

        sql = "SELECT * FROM roles WHERE uid="+str(uid)+";"
        role = query(sql)

        # 设置 JWT 令牌的有效时间为 3 分钟
        expiry_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=3)
        
        data = {'uid': uid, 'name': name, 'role': role[2], 'email': email, "exp": expiry_time}
        response['data'] = data

        response['token'] = generate_token(data)
        return response
    else:
        response['msg'] =  "密码错误"
        response['code'] = 401
        return response

def parse_token(token):
  # 定义签名密钥
  secret = 'secret-key'

  # 解码 token
  payload = jwt.decode(token, secret, algorithms=['HS256'])

  # 获取 token 中包含的过期时间
  data = payload['data']
  exp = data['exp']

  # 获取当前时间
  now = time.time()

  # 检查 token 是否已过期
  if exp < now:
    # token 已过期，拒绝访问
    print("Token has expired")
  else:
    # token 未过期，允许访问
    print("Token is valid")