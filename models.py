from db import db





class User(db.Model):
    __tablename__ = "Business Info"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Integer, nullable=False)
    career = db.Column(db.String(20), nullable=False)


    