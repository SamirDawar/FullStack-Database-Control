#contains database models and how we interact with them
from config import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_Name = db.Column(db.String(80), unique=False, nullable = False)
    Last_Name = db.Column(db.String(80), unique=False, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)

    def to_json(self):
        return {
            "id" : self.id,
           "firstName" : self.first_Name,
           "lastName" : self.last_Name,
           "email" : self.email
        }