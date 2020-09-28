'''
https://www.runoob.com/python/python-func-enumerate.html
[Python進階技巧 (6) — 迭代那件小事：深入了解 Iteration](https://medium.com/citycoddee/python%E9%80%B2%E9%9A%8E%E6%8A%80%E5%B7%A7-6-%E8%BF%AD%E4%BB%A3%E9%82%A3%E4%BB%B6%E5%B0%8F%E4%BA%8B-%E6%B7%B1%E5%85%A5%E4%BA%86%E8%A7%A3-iteration-iterable-iterator-iter-getitem-next-fac5b4542cf4)
## 描述
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
Python 2.3. 以上版本可用，2.6 添加 start 参数。

## 语法
以下是 enumerate() 方法的语法:
```
enumerate(sequence, [start=0])
```

## 参数
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
'''

'''
Example 1: 將list裡的元素結合index輸出
output: [(0, 'c'), (1, 'c++'), (2, 'c#'), (3, 'Rust'), (4, 'Java'), (5, 'Kotlin')]
'''
languages = ['c','c++','c#','Rust','Java','Kotlin']
print( list(enumerate(languages)) )

'''
Example 2: 將list與索引值對應輸出時，節省行數
等同以下效果
i:int = 0
for v in languages:
    print(f'{i},{v}')
    i+=1

output:
1,c++
2,c#
3,Rust
4,Java
5,Kotlin
'''
for i,v in enumerate(languages):
    print(f'{i},{v}')

'''
Example 3: 利用推導式輸出dict
output:{0: 'c', 1: 'c++', 2: 'c#', 3: 'Rust', 4: 'Java', 5: 'Kotlin'}
'''
print({k:v for k,v in enumerate(languages)})

'''
利用enumerate一行產生對應索引值的hash table
'''
print(dict(enumerate(languages)))