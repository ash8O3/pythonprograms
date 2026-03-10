import os
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="../templates")

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # ... your login logic ...
    return "Login attempt received"

# This line is sometimes required by certain Vercel builders
app = app
