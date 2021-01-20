#!/usr/bin/python3
"""Start Flask web app using templates"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def session_down(error):
    """Closes the database again at the end of the request"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """To display list of cities by states"""
    s = storage.all(State).values()
    return render_template('8-cities_by_states.html', s=s)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
