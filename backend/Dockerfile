# ベースイメージとして公式のPythonイメージを使用
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /app

# ソースコードをコピー
COPY . /app

# ライブラリinstall
RUN pip install --no-cache-dir -r requirements.txt

# Port 8080
EXPOSE 8080

# Flaskアプリ実行
CMD ["python", "api.py"]