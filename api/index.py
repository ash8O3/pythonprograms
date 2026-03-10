import os
from flask import Flask, render_template, request

# This line calculates the path to the root 'templates' folder
# '..' means "go up one level"
base_dir = os.path.dirname(__file__)
template_dir = os.path.abspath(os.path.join(base_dir, '..', 'templates'))

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('login.html')

# ... rest of your login logic ...
