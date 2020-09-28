'''
比較None與空字串，0，等，以及函數回傳None時的比較方法

這裡要釐清bool

https://juejin.im/post/6844903842161623054
https://zhuanlan.zhihu.com/p/65193194
'''

'''
規則一: if的空值檢查

在以下情況`if x:`敘述為false
- False
- None
- 數字如 `0`,`0.0`,`-0.0`
- 空字串 `''`, `u''`
- 空容器如 list, tuple, set, dict
- anything that implements `__bool__` (in Python3) to return False, or `__nonzero__` (in Python2) to return False or 0.
- anything that doesn't implement `__bool__` (in Python3) or `__nonzero__` (in Python2), but does implement `__len__` to return a value equal to 0

Reference
[StackOverFlow](https://stackoverflow.com/questions/20420934/if-x-vs-if-x-true-vs-if-x-is-true)
[python 邏輯值檢測](https://docs.python.org/zh-tw/3/library/stdtypes.html#truth-value-testing)
'''

'''
規則二: is 與 ==
is運算比較兩者是否為同一參考，即兩個物件的記憶體是否在同一位子
而 == 比較的是兩者的值是否相等，取決於`__eq__`方法的實作
當比較`a is b`時，不可變的變數(整數，浮點數，字串，bool，tuple)會相同，而可變的變數(list，set，dict)
'''

x_int = 0
y_int = 0
print(x_int is y_int) # True
print(x_int == y_int) # True

x_list = []
y_list = []
print(x_list is y_list) # False
print(x_list == y_list) # True

x_tuple = ()
y_tuple = ()
print(x_tuple is y_tuple) # False
print(x_tuple == y_tuple) # True

'''
規則三:
None是一個特別的物件，不等同於False,0,空字串，或其他任意空容器，同時None物件本身為單一模式
因此，當函數明確表示"失敗回傳None"時，不能用`if x`的語句，應該使用`if x is not None`更加明確
因為當x為0時`if x:`同樣不會執行
'''
y = None
print(y is not None) # True
print(y != None) # True