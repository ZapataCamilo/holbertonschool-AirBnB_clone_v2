#!/usr/bin/python3
""" Import Flask """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Script that starts a Flask web application
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Script that starts a Flask web application
    """
    return 'HBNB'


@app.route('/c/<string:username>', strict_slashes=False)
def show_user_profile(username):
    """
    display “C ” followed by the value of the text variable
    """
    # show the user profile for that user
    for i in username:
        if i == '_':
            return f"C {username.replace('_', ' '),}"
    return f'C {username}'


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def txt(text='is cool'):
    """
    script that starts a Flask web application:
    """
    for i in text:
        if i == '_':
            txt_r = text.replace('_', ' ')
            return f"Python {txt_r}"
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    display “n is a number” only if n is an integer
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_two(n=None):
    """
    display “n is a number” only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def eve_odd(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
