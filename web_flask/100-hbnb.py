#!/usr/bin/python3
"""Flask web server"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.teardown_appcontext
def poped(err):
    """called after each request finshied"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """serve hbnb_filters"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    print(list(places.values())[0].owner)
    return render_template("100-hbnb.html", states=states, places=places, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
