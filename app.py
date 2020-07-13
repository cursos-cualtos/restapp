from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    message = {'message': 'Welcome to the app!'}
    return json.dumps(message)

if __name__ == "__main__":
    app.run(port=5000)