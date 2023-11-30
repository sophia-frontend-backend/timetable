# バックエンドの起動

## 仮想環境

### Unix系

```sh
cd ./backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3 api.py
```

### Windows

```sh
cd ./backend
python -m venv venv
./venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python api.py
```

## データ作成

別のターミナルを開く

```sh
cd ./backend
source venv/bin/activate
python3 create.py
```

