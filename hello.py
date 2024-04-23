from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello world!' #simple message
    return 'Hello, World!'
