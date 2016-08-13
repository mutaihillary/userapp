#!flask/bin/python
from flask import Flask, render_template, request
from forms import LoginForm


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def home():
    return render_template('user.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


if __name__ == "__main__":
    app.run(debug=True)
