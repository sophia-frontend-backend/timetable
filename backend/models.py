from app import db

class Timetable(db.Model):
    date = db.Column(db.String(10), primary_key=True, unique=False)
    period = db.Column(db.Integer, primary_key=True, unique=False)
    classname = db.Column(db.String(100), unique=False)
    professor = db.Column(db.String(15), unique=False)
    room = db.Column(db.String(15), unique=False)