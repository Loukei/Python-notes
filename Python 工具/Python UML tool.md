## Pyreverse 工具

### 需求
閱讀一些源碼時，想直觀的看一下它的UML類關係圖。
搜索發現已有相關的軟件可以實現這個功能。

### 安裝軟件
個人開發環境：windows+vscode

- graphviz

在官網安裝即可：graphviz
注意：安裝好後，將安裝路徑添加到環境變量中。我的路徑是C:\Program Files (x86)\Graphviz2.38\bin

- pyreverse

該程序已集成在pylint模塊中，若未安裝pylint，需先安裝：pip install pylint

### 使用

#### 操作流程：

想對test.py進行類分析
在該腳本文件夾下打開cmd或powershell窗口，執行以下命令後，會在當前文件夾下生成classes.png。
`pyreverse -ASmy -o png test.py`
也可指定輸出文件名:`pyreverse -ASmy -o png -p test test.py`，運行後會生成classes_test.png。

#### 註釋：我最初執行該命令無法直接一步生成，於是分成兩步也可。

1. `pyreverse -ASmy -o dot test.py`

在命令行(python)下執行該命令，作用：pyreverse 會分析test.py中的類關係，然後生成classes.dot文件。
可指定輸出文件名:`pyreverse -ASmy -o dot -p test test.py`，運行後會生成classes_test.dot文件。
也可指定分析某個文件夾：`pyreverse -ASmy -o dot folder/`
注：看其他博客可直接一步生成圖片：`pyreverse -ASmy -o png test.py`。但我會報錯，看提示信息是：只支持輸出dot文件。那就再轉一下吧。

2. `dot -Tpng classes.dot -o test.png`

在命令行下執行該命令，作用：graphviz將.dot文件解析為圖片。

[pylint](https://pypi.org/project/pylint/)
[Pyreverse Doc](https://www.logilab.org/blogentry/6883)