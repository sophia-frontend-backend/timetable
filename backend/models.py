from app import db

class Timetable(db.Model):
    date = db.Column(db.String(2), primary_key=True)
    period = db.Column(db.Integer, primary_key=True)
    classname = db.Column(db.String(100))
    professor = db.Column(db.String(15))
    room = db.Column(db.String(15))