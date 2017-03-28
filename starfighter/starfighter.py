from flask import Flask, render_template, redirect, url_for
from flask import request, session, make_response, flash
import io
import matplotlib.pyplot as plt
from functools import wraps

from starfighter.simple_page import simple_page
from starfighter import models


app = Flask(__name__)
app.register_blueprint(simple_page)
app.secret_key = 'fake_key'


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('welcome'))


@app.route("/")
@login_required
def home():
    return render_template('home.html')


def render_page():
    my_title = "Show me the databases:"

    my_text = ""
    for row in models.read_rows():
        my_text += row[0] + "<br/>"

    my_html = my_title + "<br/>" + my_text

    return my_html


@app.route("/db")
def db_page():
    return render_page()


@app.route("/map")
def simple():

    output = io.BytesIO()

    plt.plot([1, 23, 2, 4])
    plt.ylabel('some numbers')

    output = io.BytesIO()
    plt.savefig(output)

    response = make_response(output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


if __name__ == "__main__":
    app.run()
