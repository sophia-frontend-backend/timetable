<br>

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

<<<<<<< HEAD
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

=======
>>>>>>> dd50de889ae9816de187ffc8f836772ebb79bd86
## Docker環境が利用可能な場合

```sh
docker build -t my-flask-app .
docker run --rm -p 8080:8080 my-flask-app
```