import requests
import json

base_url = "http://127.0.0.1:5000/"

# 月曜日から金曜日、periodは1から6までの組み合わせに対してPOSTリクエストを送信
for day in ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日']:
    for period in range(1, 7):
        data = {
            "date": day,
            "period": period,
            "classname": "",
            "professor": "",
            "room": ""
        }

        response = requests.post(base_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        print(response.json())