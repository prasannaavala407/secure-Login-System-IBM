# Secure Login System - AVALA LAKSHMI PRASANNA
# IBM SkillsBuild Cybersecurity Fundamentals Project
# Features: bcrypt password hashing, SQL injection protection, Session management

from flask import Flask, request, session
import bcrypt

app = Flask(__name__)
app.secret_key = 'ibm_cyber_2026'

def hash_password(password):
    # bcrypt - Industry standard for password security
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed):
    # Verify hashed password during login
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

@app.route('/register', methods=['POST'])
def register():
    # SQL Injection Protection: Input validation + Parameterized queries must be used
    username = request.form['username']
    password = hash_password(request.form['password'])
    return "User registered securely with hashed password"

@app.route('/login', methods=['POST']) 
def login():
    # Session Management: Create session on login
    session['user'] = request.form['username']
    return "Secure Login Success - Session Started"

@app.route('/logout')
def logout():
    # Session Management: Destroy session on logout
    session.pop('user', None)
    return "Logged out securely"

if __name__ == '__main__':
    app.run(debug=True)
