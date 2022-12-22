from flask import Flask, request
import sqlite3
import jwt
import query_db
import datetime
import init_db
app = Flask(__name__)

# 1. login --------------------------------------------------------------------------
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
    user = query_db.query(sql)

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
        role = query_db.query(sql)

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


# 2. editInfo --------------------------------------------------------------------------
# request
'''
{
  "new_email": "dixin.fan@mail.ustc.edu.cn",
  "new_pwd": "dixin",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjMsIm5hbWUiOiJkaXhpbi5mYW4iLCJyb2xlIjoic2FsZSIsImVtYWlsIjoiZGl4aW4uZmFuQG1haWwudXN0Yy5lZHUuY24iLCJleHAiOjE2NzE2ODU1MDl9.KGq4_MckpO5lVG5LX5rSGH4lmW_Adz6Ez1zOa4Nk_C0"
}
'''
# response
'''
{
  "code": 401,
  "msg": "token失效"
}
{
  "code": 200,
  "msg": "修改成功",
  "new_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjMsIm5hbWUiOiJkaXhpbi5mYW4iLCJyb2xlIjoic2FsZSIsImVtYWlsIjoiZGl4aW4uZmFuQG1haWwudXN0Yy5lZHUuY24iLCJleHAiOjE2NzE2ODU2NDR9.W49ZqlW2n4x1v_MH5KzMX2egZfcfJTX1txPaPPUr55M"
}
'''
@app.route("/api/editInfo", methods=["POST"])
def editInfo():
    # Retrieve the user data from the request
    params = request.get_json()
    new_email = params["new_email"]
    new_pwd = params["new_pwd"]
    token = params["token"]

    response = {}
    flag, data = parse_token(token)
    if not flag:
      response['msg'] =  "token失效"
      response['code'] = 401
      return response
    
    # uid = int(data['uid'])
    uid = str(data['uid'])
    if new_pwd == "":
      sql = "UPDATE users SET email = '" +new_email+"' WHERE uid = "+uid;
    else:
      sql = "UPDATE users SET email = '" +new_email+"', pwd = '"+new_pwd+"' WHERE uid = "+uid;

    response['msg'] =  "修改成功"
    response['code'] = 200
    try:
      init_db.execute_sql(sql)
    except Exception as e:
      response['msg'] =  "服务器内部错误"
      response['code'] = 500
      return response
    
    data['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=3)
    new_token = generate_token(data)
    response['new_token'] = new_token
    response['new_email'] = new_email

    return response


def parse_token(token):
  # 定义签名密钥
  secret = 'secret-key'
  flag, data = False, None

  try:
    # 解码 token
    payload = jwt.decode(token, secret, algorithms=['HS256'])
  except:
    return flag, data

  # 获取 token 中包含的过期时间
  exp = payload['exp']
  # 获取当前时间
  now = datetime.datetime.utcnow().timestamp()
  # 检查 token 是否已过期
  if exp >= now:
    # token 未过期，允许访问
    flag = True
    data = payload
    
  return flag, data