import requests
import json

URL = "http://127.0.0.1:8080"
DATE_LIST = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日"]
PERIOD_LIST = list(range(1, 7))
# TIMETABLE_URL = os.path.join(URL, f'timetable/{DATE}/{PERIOD}')

TIMETABLES = []
for date in DATE_LIST:
    for period in PERIOD_LIST:
        TIMETABLES.append(
            {'date': date, 'period': period, 'classname': "", 'professor': "", 'room': ''}
            )

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
    print(f"POST content: {json.loads(response.json())}")

    # GET A USER 
    response = requests.get(TIMETABLE_URL)
    print(f"\nGET url: {response.url}")
    print(f"content: {json.loads(response.json())}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")
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
    print(f"content: {json.loads(response.json())}\n")
    # --------------------------------------------------------

    # DELETE A USER DATA
    # --------------------------------------------------------
    # DELETE ID
    response = requests.delete(TIMETABLE_URL)
    print(f"\nDELETE url: {response.url}")
    print(f"content: {json.loads(response.json())}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")
    # CHANGE A USER DATA 
    # --------------------------------------------------------

def main():
    make_sample_timetables()
    # make_timetable()

if __name__ == '__main__':
    main()