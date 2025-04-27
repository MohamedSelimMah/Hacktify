from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS users')
    c.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', 'adminpass'))
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # VULNERABLE QUERY: SQL Injection possible
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print(f"Executing query: {query}")  # Debugging - print query

    c.execute(query)
    result = c.fetchone()
    conn.close()

    if result:
        flag = "FLAG{SQLI_SUCCESS_123}"
        return render_template('success.html', flag=flag)
    else:
        return "Login failed."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
