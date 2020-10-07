## python指令

`python --version`: 查詢python版本

## pip指令

`pip install flask`: 安裝flask模組

`pip install -U flask`: 更新套件

`pip uninstall flask`: 移除安裝過的套件

`pip install -v flask==1.0`: 安裝並且指定套件版本

`pip list`: 查看目前安裝過的清單

**使用 pip 一次安裝多個套件**

每次換環境就需要重新安裝套件，輸入指令重新安裝很麻煩，所以我們通常都會將要安裝的套件寫在 txt 檔案裡面，只需要 install 這個文字檔就可以一次安裝所有需要的套件囉！

`pip install -r requirements.txt`: pip 安裝 requirements.txt 內的清單

`pip freeze > requirements.txt`: 將安裝過的套件建立成 requirements.txt 文件清單
