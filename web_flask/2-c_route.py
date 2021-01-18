#!/usr/bin/python3
"""Start Flask web app with three routes"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """To display a message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """To display a message"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """to display text"""
    return "C %s" % text.replace("_", " ")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
