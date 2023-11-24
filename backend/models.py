from app import db

class Timetable(db.Model):
    date = db.Column(db.String(10), primary_key=True, unique=False, nullable=True)
    period = db.Column(db.Integer, primary_key=True, unique=False, nullable=True)
    classname = db.Column(db.String(100), unique=False, nullable=True)
    professor = db.Column(db.String(15), unique=False, nullable=True)
    room = db.Column(db.String(15), unique=False, nullable=True)