#!/usr/bin/python3
"""Start Flask web app using templates"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """To display States"""
    n = storage.all(State).values()
    return render_template('7-states_list.html', n=n)


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
