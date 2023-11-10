from app import db

class Timetable(db.Model):
    date = db.Column(db.String(2), primary_key=True)
    period = db.Column(db.Integer, unique=True, primary_key=True)
    classname = db.Column(db.String(100), unique=True)
    professor = db.Column(db.String(15), unique=True)
    room = db.Column(db.Integer, unique=True)