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