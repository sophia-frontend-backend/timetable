<br>

# バックエンドの起動

バックエンドの環境構築についてです。

<br>

## ローカルで環境構築する場合

```sh
cd ./backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3 api.py
```

<br>

## Docker環境が利用可能な場合

```sh
docker build -t my-flask-app .
docker run --rm -p 8080:8080 my-flask-app
```