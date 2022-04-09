from flask import Flask
app = Flask(__name__)
@app.route('/home')
def hello():
    return 'Welcome to My Watchlist!'
