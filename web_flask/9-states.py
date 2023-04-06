#!/usr/bin/python3
''' starts a Flask web application'''
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<path:id>', strict_slashes=False)
def path_st_list(id):
    st = storage.all(State).values()

    if not id:
        return render_template('7-states_list.html', items=st)

    r_st = 'State.{}'.format(id)
    if r_st in st:
        return render_template(
            '9-states.html',
            st='State" {}'.format(st[r_st].name),
            items=st[r_st])

    return render_template('9-states.html', item=None)


@app.teardown_appcontext
def teardown_db(exception):
    '''remove the current SQLAlchemy Session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
