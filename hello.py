import requests
from flask import Flask
# Initial Flask application
app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# this does the same thing as the command line flask --app  hello run
# if __name__ == "__main__":
#     app.run()