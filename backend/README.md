# バックエンドの軌道

```sh
cd ./backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3 api.py
```

別のターミナルを開く

```sh
cd ./backend
source venv/bin/activate
python3 test.py
```

#curl コマンド
```sh
POST   : curl -X POST -H "Content-Type: application/json" -d '{＃json型で内容}' http://localhost:5000/
PUT    : curl -X PUT -H "Content-Type: application/json" -d '{＃json型で内容}' http://localhost:5000/#DATE/#PERIOD
GET    : curl http://localhost:5000/
DELETE : curl -X DELETE http://localhost:5000/
```
