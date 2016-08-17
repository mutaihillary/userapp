#!flask/bin/python
from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_login import login_user
from forms import LoginForm
from  forms import Logout
import models

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'hdhdhdhd.jhjhjhjh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/')
def home():
    return render_template('user.html')


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
            return redirect(url_for("index"))
    return render_template("user.html", form=form)


"""@bull.route("/logout", methods=["GET"])
@login_required
def logout():
    Logout the current user.
    models.User = current_user
    models.user.authenticated = False
    models.db.session.add(user)
    models.db.session.commit()
    logout_user()
    return render_template("logout.html")
"""


@app.route('/display', methods=['POST', 'GET'])
def display():
    if request.method == 'POST':
        display = request.form
    return render_template("display.html", display=display)


if __name__ == "__main__":
    app.run(debug=True)
