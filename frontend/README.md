# Frontendの起動

## node.jsがinstallされている場合

```sh
cd frontend
npm install
npm run dev
```

## Dockerの環境がある場合

```sh
docker build -t my-vue-app .
docker run --rm -p 3000:3000 my-vue-app
```