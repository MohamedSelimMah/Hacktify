from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    score = db.Column(db.Integer, default=0)

class Lab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    flag = db.Column(db.String(120), nullable=False)
    points = db.Column(db.Integer, nullable=False)
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
    return render_template('login')

@app.route('/vulnerable_login', methods=['POST'])
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
