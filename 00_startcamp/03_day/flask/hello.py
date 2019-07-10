from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "everything is changed"

@app.route('/ssafy/')
def ssafy():
    return "This is ssafy!"