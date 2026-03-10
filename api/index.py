import os
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="../templates")

# Simple user data
USER_DATA = {"admin": "password123"}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username in USER_DATA and USER_DATA[username] == password:
        return f"<h1>Success!</h1><p>Welcome back, {username}.</p>"
    else:
        return "<h1>Error</h1><p>Invalid credentials.</p>", 401

# IMPORTANT: Do NOT add app.run() here. 
# Vercel handles the execution for you.
