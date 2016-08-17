from flask_sqlalchemy import SQLAlchemy
from run import app

db = SQLAlchemy(app)


# create a user model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.column(db.String)
    dob = db.column(db.DateTime)
    location = db.column(db.String)

    def __init__(self, first_name, last_name, dob, location):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.location = location

    def __repr__(self, first_name, last_name, dob, location):
        return self.first_name, self.last_name, self.dob, self.location



