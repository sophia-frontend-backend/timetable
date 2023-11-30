from app import db
from models import Timetable

def create_timetable():

    DATE_LIST = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日"]
    PERIOD_LIST = list(range(1, 7))

    db.session.query(Timetable).delete()

    for date in DATE_LIST:
        for period in PERIOD_LIST:
            timetable = Timetable(
                date = date,
                period = period,
                classname = "",
                professor = "",
                room = "",
            )
            db.session.add(timetable)
            db.session.commit()