import sqlite3

def query(sql):
    conn = sqlite3.connect("pfm.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    conn.close()
    return result