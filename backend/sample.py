import requests
import json
import os

URL = "http://127.0.0.1:5000/"

TIMETABLES = [
    {'date': "月曜日", 'period':1 , 'classname': "", 'professor': "", 'room': ''},
    # {'date': "月曜日", 'period': 2, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "月曜日", 'period': 3, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "月曜日", 'period': 4, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "月曜日", 'period': 5, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "月曜日", 'period': 6, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "火曜日", 'period': 1, 'classname': "", 'professor': "", 'room': ''},
     {'date': "火曜日", 'period': 2, 'classname': "1", 'professor': "1", 'room': '1'},
    # {'date': "火曜日", 'period': 3, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "火曜日", 'period': 4, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "火曜日", 'period': 5, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "火曜日", 'period': 6, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "水曜日", 'period': 1, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "水曜日", 'period': 2, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "水曜日", 'period': 3, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "水曜日", 'period': 4, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "水曜日", 'period': 5, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "水曜日", 'period': 6, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "木曜日", 'period': 1, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "木曜日", 'period': 2, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "木曜日", 'period': 3, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "木曜日", 'period': 4, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "木曜日", 'period': 5, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "木曜日", 'period': 6, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "金曜日", 'period': 1, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "金曜日", 'period': 2, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "金曜日", 'period': 3, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "金曜日", 'period': 4, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "金曜日", 'period': 5, 'classname': "", 'professor': "", 'room': ''},
    # {'date': "金曜日", 'period': 6, 'classname': "", 'professor': "", 'room': ''}
    ]
for timetable in TIMETABLES:
        response = requests.post(URL, data=json.dumps(timetable))
        print(f"status code: {response.status_code}")
        print(f"content: {response.json()}")