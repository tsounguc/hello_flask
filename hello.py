import requests
from flask import Flask
# Initial Flask application
app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"

# this does the same thing as the command line flask --app  hello run
if __name__ == "__main__":
    app.run(debug=True)
