# Put your app in here.
from flask import Flask, request
app = Flask(__name__)


@app.route("/welcome")
def welcome_empty():
    return f"welcome"

@app.route("/welcome/<place>")
def welcome_statement(place):
    return f"welcome {place}"