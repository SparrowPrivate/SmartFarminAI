from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello there! The webapp is working"
