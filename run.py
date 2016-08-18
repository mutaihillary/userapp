#!flask/bin/python
from flask import Flask, render_template, request, redirect, url_for,flash
from flask_bcrypt import Bcrypt
from flask_login import login_user
from forms import LoginForm, RegistrationForm
import sqlite3 as sql
import models
from __init__ import db


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'hdhdhdhd.jhjhjhjh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """For GET requests, display the login form. For POSTS, login the current user
        by processing the form."""
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.get(form.email.data)
        if user:
            if Bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                models.db.session.add(user)
                models.db.session.commit()
                login_user(user, remember=True)
            return redirect(url_for("home"))
    return render_template("login.html", form=form)

con = sql.connect('userapp.db')
# register a user


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form)
    if form.validate_on_submit():
        user = models.User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('user.html', form=form)


"""""
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
"""""


@app.route('/user')
def user():
    con = sql.connect("userapp.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from user")

    rows = cur.fetchall()
    return render_template("user.html", rows=rows)


@app.route('/display', methods=['POST', 'GET'])
def display():
    if request.method == 'POST':
        display = request.form
    return render_template("display.html", display=display)


if __name__ == "__main__":
    app.run(debug=True)
