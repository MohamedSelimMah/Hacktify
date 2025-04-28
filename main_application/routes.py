from flask import request, jsonify, session
from mdoels import User, db
from app import app

FLAG = "FLAG{basic_sql_injection}"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"message": "Username and password required"}), 400
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "User already exists"}), 400
    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Registered successfully"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"message": "Username and password required"}), 400
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        session['username'] = user.username
        return jsonify({"message": "Logged in successfully"})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/submit_flag', methods=['POST'])
def submit_flag():
    if 'username' not in session:
        return jsonify({"message": "Unauthorized"}), 401
    data = request.get_json()
    if data.get('flag') == FLAG:
        user = User.query.filter_by(username=session['username']).first()
        user.score += 100
        db.session.commit()
        return jsonify({"message": "Correct flag! Points awarded"})
    return jsonify({"message": "Incorrect flag"}), 400
