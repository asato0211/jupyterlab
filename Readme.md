# JupyterLab

- リスト抽出
- データ分析

## 起動方法

### コマンド実行
```
docker-compose build
docker-compose up
```

### ブラウザ表示
```
lab  | [I 2024-02-25 05:33:50.003 ServerApp] Jupyter Server 2.12.5 is running at:
lab  | [I 2024-02-25 05:33:50.003 ServerApp] http://201e3fb66e4f:18888/lab?token=7ea559239ca8113401dff888bd4b168d3d46e0c040cc326b
lab  | [I 2024-02-25 05:33:50.003 ServerApp]     http://127.0.0.1:18888/lab?token=7ea559239ca8113401dff888bd4b168d3d46e0c040cc326b <-- cmd + クリック
lab  | [I 2024-02-25 05:33:50.003 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
lab  | [C 2024-02-25 05:33:50.005 ServerApp]
```

http://127.0.0.1:18888/lab?token=[トークン]の部分をコピーしてurlに貼り付けて起動

## ファイルの格納方法

- フォルダ名をつけて直下にmain.ipynbを追加する

```
[フォルダ名]/main.ipynb
```

## パッケージの追加方法
- requirements.txtに欲しいパッケージを記載
- コンテナ内部で`pip3 install -r requirements.txt`を実行
