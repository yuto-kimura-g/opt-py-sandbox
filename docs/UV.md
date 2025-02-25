# UV

```console
$ mkdir <project>
$ cd <project>
$ uv init -p 3.11 # latest(3.13) だと対応していないpackageがあるので、少し古めのやつ
$ uv add <package> # .venv を自動作成して、.vnev に追加する
$ uv sync # git clone した後とか
$ uv pip list
$ uv python hello.py # .venv で実行
$ source .venv/bin/activate && python hello.py # こうしてもいいけど
```
