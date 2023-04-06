#!/usr/bin/python3
""" Import Flask """
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def st_list():
    stg = storage.all(State).values()
    return render_template('7-states_list.html', stg=stg)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
