from flask import Flask
from markupsafe import escape
import json

app = Flask(__name__)

@app.route('/')
def index():
    message = {'message': 'Welcome to the app!'}
    return json.dumps(message)

@app.route('/greeting')
def greeting():
    message = {'message': 'Hello user'}
    return json.dumps(message)

@app.route('/greeting/<string:name>')
def gretting_by_name(name):
    message = {'message': 'Hello ' + name}
    return json.dumps(message)

@app.route('/add', methods=['GET', 'POST'])
def add():
    return ''

if __name__ == "__main__":
    app.run(port=5000)