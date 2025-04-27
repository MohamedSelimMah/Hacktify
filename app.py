import csv

from flask import Flask,request
import sqlite3

app = Flask(__name__)

def init__db():
    connection= sqlite3.connect('users.db')
    c=connection.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARYKEY, username TEXT, password TEXT)')
    c.execute('INSERT INTO users (username,password) VALUES (?,?)',('admin','adminpass'))
    connection.commit()
    connection.close()

init__db()

@app.route('/')
def home():
    return'''
            <h2>Login Frame</h2>
            <form action="/login" method="post">
            username: <input type="text" name="username"><br>
            password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
            </form>
    '''

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    connection= sqlite3.connect('users.db')
    c = connection.cursor()

    query=f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print(query)
    c.execute(query)
    result= c.fetchone()
    connection.close()

    if result:
        return "Login Success FLAG{HDM_231jfel8_HACKTIFY}"
    else:
        return "Login Failed."


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)