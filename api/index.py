from flask import Flask, render_template, request, redirect, url_status

app = Flask(__name__)

# Dummy credentials for demonstration
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
    else:
        return "Invalid credentials. Please try again.", 401

if __name__ == '__main__':
    app.run(debug=True)
