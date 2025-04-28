from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

FLAG = "FLAG{basic_sql_injection}"

DB_FILE = 'vuln.db'

def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, secret TEXT)')
        c.execute('INSERT INTO users (username, secret) VALUES (?, ?)', ('admin', FLAG))
        conn.commit()
        conn.close()

@app.route('/')
def home():
    return 'Welcome to the Vulnerable Lab! Try /search_user?username=...'

@app.route('/search_user')
def search_user():
    username = request.args.get('username', '')
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # Intentionally vulnerable to SQLi
    query = f"SELECT secret FROM users WHERE username = '{username}'"
    try:
        c.execute(query)
        result = c.fetchone()
    except Exception as e:
        return f"Query Error: {e}"
    conn.close()
    if result:
        return f"Found: {result[0]}"
    return "User not found."

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001, debug=True)
