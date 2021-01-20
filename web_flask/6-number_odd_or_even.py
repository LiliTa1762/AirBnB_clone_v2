#!/usr/bin/python3
"""Start Flask web app using templates"""


from flask import Flask, render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """To display if n is number"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """To display HTML page if n is int"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """To display HTML page if n is odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
