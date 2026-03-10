from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Login Page</h2>
    <form action="/login" method="POST">
        <input type="text" name="u" placeholder="Username"><br>
        <input type="password" name="p" placeholder="Password"><br>
        <button type="submit">Login</button>
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    return "<h1>Login Successful</h1>"

# This ensures Vercel can find the 'app' object
app = app
