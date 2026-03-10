from flask import Flask, request

app = Flask(__name__)

# The HTML is now inside the Python file as a string
LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
    <style>
        body { font-family: sans-serif; display: flex; justify-content: center; padding-top: 50px; background-color: #f4f4f9; }
        .login-card { border: 1px solid #ccc; padding: 20px; border-radius: 8px; width: 300px; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        input { width: 100%; margin-bottom: 10px; padding: 8px; box-sizing: border-box; border: 1px solid #ddd; border-radius: 4px; }
        button { width: 100%; padding: 10px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <div class="login-card">
        <h2>Login</h2>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Log In</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return LOGIN_HTML

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "admin" and password == "password123":
        return "<h1>Success!</h1><p>Welcome back, admin.</p>"
    return "<h1>Error</h1><p>Invalid credentials.</p><a href='/'>Try again</a>", 401
