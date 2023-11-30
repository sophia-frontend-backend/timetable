<br>

# フロントエンドの起動

フロントエンドの環境構築についてです。

<br>

## node.jsがinstallされている場合

```sh
cd frontend
npm install
npm run dev
```

<br>

## Dockerの環境がある場合

```sh
docker build -t my-vue-app .
docker run --rm -p 3000:3000 my-vue-app
```