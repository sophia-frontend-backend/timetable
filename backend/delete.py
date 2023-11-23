import requests
import json
import os

URL = "http://127.0.0.1:5000"

def delite():
    # DELETE USERS
    response = requests.delete(URL)
    print(f"\nDELETE url: {response.url}")
    print(f"DELETE content: {response.json()}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {response.json()}\n")
    
if __name__ == '__main__':
    delite()


