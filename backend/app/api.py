from flask import request
from flask_restful import Resource, Api
import json
from app import app, db
from models import Timetable

class AllTimetables(Resource):
    def get(self):
        try:
            timetables = db.session.query(Timetable).all()
            timetables_list = []
            for timetable in timetables:
                timetables_list.append(
                    {
                        "date": str(timetable.date),
                        "period": str(timetable.period),
                        "classname": str(timetable.classname),
                        "professor": str(timetable.professor),
                        "room": str(timetable.room),
                    }
                )
            response = {
                'status': "ALLGOT",
                'timetabels': timetables_list,
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "error": str(e)
                }

        return json.dumps(response)
    
    def post(self):
        try:
            data = json.loads(request.data)
            timetable = Timetable(
                date = data["date"],
                period = data["period"],
                classname = data["classname"],
                professor = data["professor"],
                room = data["room"],
            )
            db.session.add(timetable)
            db.session.commit()

            response = {
                'status': "POSTED",
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }
            
        return json.dumps(response)

    def delete(self):
        try:
            db.session.query(Timetable).delete()
            db.session.commit()

            response = {
                'status': "ALLDELETE",
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }
            
        return json.dumps(response)
    
class TimetableApi(Resource):
    def get(self, date, period):
        try:
            timetable = db.session.query(Timetable).get(date, period)
            response = {
                "status": "GOT",
                'date': timetable.date,
                'period': timetable.period,
                'classname': timetable.classname,
                'professor': timetable.professor,
                'room': timetable.room,
                
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }

        return json.dumps(response)
    
    def put(self, date, period):
        try:
            timetable = db.session.query(Timetable).get(date, period)
            put_data = json.loads(request.data)
            timetable.classname = put_data["classname"]
            timetable.professor = put_data["professor"]
            timetable.room = put_data["room"]
            db.session.add(timetable)
            db.session.commit()

            response = {
                'status': "PUT",
                }

        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }

        return json.dumps(response)
    
    def delete(self, date, period):
        try:
            timetable = db.session.query(Timetable).filter_by(date=date, perid=period)
            timetable.delete()
            db.session.commit()

            response = {
                'status': "DELETE",
                }

        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }

        return json.dumps(response)

if __name__ == '__main__':
    api = Api(app)

    api.add_resource(AllTimetables, '/')
    api.add_resource(TimetableApi, '/timetable/<date>/<int:period>')

    with app.app_context():
        db.create_all()
    
    app.run (debug=True)