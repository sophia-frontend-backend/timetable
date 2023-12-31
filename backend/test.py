import requests
import json
import os

URL = "http://127.0.0.1:5000"
DATE = "月曜日"
PERIOD =1
TIMETABLE_URL = os.path.join(URL, f'timetable/{DATE}/{PERIOD}')

TIMETABLES = [
    {'date': "金曜日", 'period': 2, 'classname': "情報リテラシー", 'professor': "川端教授", 'room': '6-201'},
    {'date': "火曜日", 'period': 5, 'classname': "生と死", 'professor': "山下教授", 'room': '12-401'},
]
POST_DATA = {
    'date': '月曜日',
    'period': 1,
    'classname': 'キリスト教',
    'professor': '宮本教授',
    'room': '2-501'

}
PUT_DATA = {
    'classname': 'sampleClass',
    }
print(TIMETABLES)
def make_sample_timetables():
    print("\nmake_sample_timetables")

    # RESET USERS DATA 
    # --------------------------------------------------------
    # DELETE USERS
    response = requests.delete(URL)
    print(f"\nDELETE url: {response.url}")
    print(f"DELETE content: {response.json()}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {response.json()}\n")
    # --------------------------------------------------------

    # CREATE USERS
    # --------------------------------------------------------
    # POST SAMPLE USERS
    for timetable in TIMETABLES:
        response = requests.post(URL, data=json.dumps(timetable))
        print(f"status code: {response.status_code}")
        print(f"content: {response.json()}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nGET url: {response.url}")
    print(f"GET content: {response.json()}")
    # --------------------------------------------------------

def make_timetable():
    print("\n\nmake_timetable")

    # CREATE A USER
    # --------------------------------------------------------
    # POST
    response = requests.post(URL, data=json.dumps(POST_DATA))
    print(f"\nPOST url: {response.url}")
    print(f"POST DATA: {POST_DATA}")
    print(f"POST content: {response.json()}")

    # GET A USER 
    response = requests.get(TIMETABLE_URL)
    print(f"\nGET url: {response.url}")
    print(f"content: {response.json()}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {response.json()}\n")
    # --------------------------------------------------------

    # CHANGE A USER
    # --------------------------------------------------------
    # PUT ID
    response = requests.put(TIMETABLE_URL, data=json.dumps(PUT_DATA))
    print(f"\nPUT url: {response.url}")
    print(f"PUT DATA: {PUT_DATA}")
    print(f"content: {response.json()}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {response.json()}\n")
    # --------------------------------------------------------

    # DELETE A USER DATA
    # --------------------------------------------------------
    # DELETE ID
    response = requests.delete(TIMETABLE_URL)
    print(f"\nDELETE url: {response.url}")
    print(f"content: {response.json()}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {response.json()}\n")
    # CHANGE A USER DATA 
    # --------------------------------------------------------

def main():
    make_sample_timetables()
    make_timetable()

if __name__ == '__main__':
    main()
