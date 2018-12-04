from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/<name>")
def name(name):
    return 'Hello <i>{}</i>!'.format(name.upper())
