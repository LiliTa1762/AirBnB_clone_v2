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


@app.route('/hbnb_filters', strict_slashes=False)
def states_id():
    """To display State object found with the id"""
    return render_template("10-hbnb_filters.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
