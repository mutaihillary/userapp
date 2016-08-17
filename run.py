#!flask/bin/python
from flask import Flask, render_template, request, login_user
from forms import LoginForm


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'hdjshjdbdshbfd.jndsjdbjbdj'


@app.route('/')
def home():
    return render_template('user.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """For GET requests, display the login form. For POSTS, login the current user
        by processing the form."""
    print user.db
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("bull.reports"))
    return render_template("login.html", form=form)


@app.route('/display', methods=['POST', 'GET'])
def display():
    if request.method == 'POST':
        display = request.form
    return render_template("display.html", display=display)


if __name__ == "__main__":
    app.run(debug=True)
