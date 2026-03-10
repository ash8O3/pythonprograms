import os
from flask import Flask, render_template, request

# This tells Flask to look for templates in the correct folder relative to this file
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

USER_DATA = {"admin": "password123"}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in USER_DATA and USER_DATA[username] == password:
        return f"Welcome back, {username}!"
    return "Invalid credentials", 401
