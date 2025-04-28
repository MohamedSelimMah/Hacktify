from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For session management and flash messages


# Initialize database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    score INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()


# Initialize the database (only run this once)
init_db()


# Home Route
@app.route('/')
def home():
    return render_template('home.html')


# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user already exists
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=?', (username,))
        user = c.fetchone()

        if user:
            flash('Username already exists. Please choose another one.', 'danger')
        else:
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            flash('Registration successful! You can now login.', 'success')
            return redirect(url_for('login'))

        conn.close()

    return render_template('register.html')


# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            return redirect(url_for('dashboard', username=username))
        else:
            flash('Invalid login credentials. Please try again.', 'danger')

    return render_template('login.html')


# Dashboard Route
@app.route('/dashboard/<username>')
def dashboard(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT score FROM users WHERE username=?', (username,))
    score = c.fetchone()
    conn.close()

    return render_template('dashboard.html', username=username, score=score[0])

@app.route('/sql_lab')
def sql_lab():
    # Render the home.html template inside sqli_labs/templates/
    return redirect('http://192.168.1.17:5000')

if __name__ == "__main__":
    app.run(debug=True)
