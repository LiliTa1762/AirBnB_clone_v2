#!/usr/bin/python3
"""Start Flask web app with routes"""


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


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_cool(text):
    """To display text by default"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<n>", strict_slashes=False)
def is_number(n):
    """To display if n is number"""
    if n.isdigit():
        return ("{} is a number".format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
