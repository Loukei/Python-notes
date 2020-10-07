# 部屬你的python程式碼

幾個可用的模組:

## PyInstaller

1. 透過 pip 安裝 pyinstaller:

`pip install pyinstaller`

2. 打包指令(-F 打包成一個exe文件)

- pyinstaller -h 查參數
- icon=更換icon參數 ( pyinstaller -F — icon=my.ico x.py) 需在同一層
- F 打包成一个exe文件
`pyinstaller -F x.py`

3. 打包後的檔案生成物

會先建立一個 hello.spec
建立「build」 資料夾 — 內涵 log 記錄檔
建立 「dist 」資料夾 — 內涵打包好的exe

建立了一些資料夾及檔案，打包成功後去 /dist 就可以找到 exe 囉

## Nuitka

將python轉為c++代碼再將其打包

[How can I make a Python script standalone executable to run without ANY dependency?](https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen)

[將 python檔案打包成exe](https://medium.com/cubemail88/%E5%B0%87python%E6%AA%94%E6%A1%88%E6%89%93%E5%8C%85%E6%88%90exe-a7d30e43676d)

[打包你的Python程式~PyInstaller基礎篇](https://www.coderbridge.com/@WeiHaoEric/0b2ced0696cc4c38a62d7b26fa7bbea0)
