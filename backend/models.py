from app import db


class Timetable(db.Model):
    date = db.Column(db.String(10), primary_key=True, unique=False, nullable=True)
    period = db.Column(db.Integer, primary_key=True, unique=False, nullable=True)
    classname = db.Column(db.String(100), unique=False, nullable=True)
    professor = db.Column(db.String(15), unique=False, nullable=True)
    room = db.Column(db.String(15), unique=False, nullable=True)

from sqlalchemy.dialects.sqlite import insert
from models import Timetable
from flask import request
from app import app

@app.route('/insert_timetable', methods=['POST'])
def insert_timetable():
    data = request.json  # ここで適切なリクエストデータを取得すると仮定

    # 一意性制約に違反した場合、何を行うかを指定
    stmt = insert(Timetable).values(data).on_conflict_do_nothing()

    db.session.execute(stmt)
    db.session.commit()

    return 