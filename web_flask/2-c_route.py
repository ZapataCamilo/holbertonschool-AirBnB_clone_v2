#!/usr/bin/python3
""" Import Flask """
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    """
    Script that starts a Flask web application
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Script that starts a Flask web application
    """
    return 'HBNB'


@app.route('/c/<username>')
def show_user_profile(username):
    """
    display “C ” followed by the value of the text variable
    """
    # show the user profile for that user
    for i in username:
        if i == '_':
            return f"C {username.replace('_', ' ')}"
    return f'C {username}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
