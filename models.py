from flask_sqlalchemy import SQLAlchemy
from run import app

db = SQLAlchemy(app)


# create a user model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.column(db.String)
    passsword = db.column(db.String)
    # dob = db.column(db.DateTime)
    # location = db.column(db.String)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return self.username



