import sqlite3


def execute_sql(sql):
    conn = sqlite3.connect("pfm.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def init_users():
    # 1.create users table in db
    execute_sql("CREATE TABLE users (uid INTEGER PRIMARY KEY,name TEXT NOT NULL,pwd TEXT NOT NULL,email TEXT NOT NULL);")

    # 2.insert users into table users
    sqls = [
        "INSERT INTO users VALUES (1, 'xin.jin', 'xin', 'xin.jin@gf.com.cn');",
        "INSERT INTO users VALUES (2, 'jiaqi.jiang', 'jiaqi', 'jiaqi.jiang@gf.com.cn');",
        "INSERT INTO users VALUES (3, 'dixin.fan', 'dixin', 'dixin.fan@mail.ustc.edu.cn');"
    ]
    for sql in sqls:
        execute_sql(sql)

def init_roles():
    execute_sql("CREATE TABLE roles (rid INTEGER PRIMARY KEY,uid INTEGER,role TEXT NOT NULL);")

    sqls = [
        "INSERT INTO roles VALUES (1, 1, 'head');",
        "INSERT INTO roles VALUES (2, 2, 'head');",
        "INSERT INTO roles VALUES (3, 3, 'sale');"
    ]
    for sql in sqls:
        execute_sql(sql)