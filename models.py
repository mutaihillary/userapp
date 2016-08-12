from flask_sqlalchemy import SQLAlchemy
from run import app

db = SQLAlchemy(app)


# create a user model
class User(db.Model):
    FirstName = db.Column(db.String(50), unique=True)
    LastName = db.column(db.string(50)),
    DOB = db.column(db.date(50)),
    Location = db.column(db.string(50))

    def __init__(self,FirstName, LastName, DOB, Location):
        self.FirstName = FirstName
        self.LastName = LastName
        self.DOB = DOB
        self.Location = Location



