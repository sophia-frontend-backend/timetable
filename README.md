<!-- # Git

```sh
git clone https://github.com/sophia-frontend-backend/timetable.git
```

```sh
git add .
git commit -m "メッセージ"
git push
```

```sh
git pull
``` -->

<!-- # frontend

```sh
cd frontend
# npm install
npm run dev
ctrl+C
cd ..
``` -->
# 1 Gitのセッティング

## 1.1 初めてセッティングする場合

```sh
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/frontend-develop-sophia/sample.git
git push -u origin main
```

## 1.2 初めてプロジェクトコードをダウンロードする場合

```sh
git clone https://github.com/frontend-develop-sophia/sample.git
cd ./sample
```

## 1.3 変更を更新して、pushする場合

```sh
git add .
git commit -m "message"
git push -u origin main
```

## 1.4 誰かの変更(リポジトリ)をもってくる場合

```sh
git pull
```

<br>

# 2 Vite proj

```sh
cd ./project
npm init vite-app frontend
cd frontend
npm install
npm install url parseurl
npm install router
npm install vuex
npm install axios
```
```sh
npm run dev
npm run build
```

<br>

# 3 ブランチ


## 3.1 ブランチの作り方

```sh
git branch <branch名>
※まだブランチを作成しただけで切り替えられていない

git branch
※ブランチの一覧を表示
※*がついてるのが今いるブランチ
```

## 3.2 ブランチの切り替えかた

```sh
git checkout <branch名>
※既存のブランチに切り替える

git checkout -b <brach名>
※新規ブランチを作成し，切り替えも行う
```

## 3.3 ブランチのマージの仕方

```sh
git merge <branch名>
※自身がいるブランチに"ブランチ名"をマージすることができる
```

## 3.4 ブランチの削除の仕方

```sh
git branch -d ブランチ名
```
