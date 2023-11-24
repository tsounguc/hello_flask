import requests
from flask import Flask

# Initial Flask application
app = Flask(__name__)

print(__name__)


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Happy Thanksgiving!</h1>' \
           '<p style="text-align: center">Yay Vegans!</p>' \
           '<img src="https://media0.giphy.com/media/m6ghJgaPsA8WgMccSm/giphy.gif?cid=ecf05e47s66zqbv351llv9q8rhea4kswp0v8usu8wbvj1zf2&ep=v1_gifs_search&rid=giphy.gif&ct=g" width=200>'


def make_bold(function):
    def wrapper_function():
        str = function()
        return f"<b>{str}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        str = function()
        return f"<em>{str}</em>"

    return wrapper_function


def make_underline(function):
    def wrapper_function():
        str = function()
        return f"<u>{str}</u>"

    return wrapper_function

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"


# this does the same thing as the command line flask --app  hello run
if __name__ == "__main__":
    app.run(debug=True)
