#!/usr/bin/python3
"""Start Flask web app using templates to list several items"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ To display the list of all State objects"""
    s = storage.all(State).values()
    return render_template("9-states.html", s=s)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """To display State object found with the id"""
    s = storage.all(State).values()
    c = storage.all(City).values()
    return render_template("9-states.html", id=id, s=s, c=c)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
