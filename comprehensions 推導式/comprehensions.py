'''
整理各種python表達式，生成list set dict的技巧
itertools --- 为高效循环而创建迭代器的函数 https://docs.python.org/zh-cn/3/library/itertools.html
'''
from typing import List

# List comprehensions
print([ i for i in range(10)]) 
'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
print([i for i in range(10) if i % 2 == 1]) 
'''
加入判斷式輸出 [1, 3, 5, 7, 9]
'''
print([i*2 for i in range(10)]) 
'''
輸出的資料不一定要與來源一樣 [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
'''
print([j for i in range(2, 8) for j in range(i*2, 50, i)])
'''
等同以下效果
li:List[int] = []
for i in range(2,8):
    for j in range(i*2, 50, i):
        li.append(j)
print(li)
'''
print([(i,j) for i in range(5) for j in range(3)]) 
'''
(i,j)組成的list，i = 0-4,j = 0-2
'''

# Set 
print( {i for i in range(4)} )
'''
{0, 1, 2, 3}
'''
print( {c for c in "Hallo world"} )
'''
{'o', ' ', 'l', 'a', 'd', 'w', 'H', 'r'}
'''
print({x for x in 'abracadabra' if x not in 'abc'})
'''
{'d', 'r'}
'''

# Dict
mca = {'a':0,'b':1,'c':3,'d':5,'e':7}
# print({v:k for k,v in mca.items()})
'''
反轉mca的key與value
{0: 'a', 1: 'b', 3: 'c', 5: 'd', 7: 'e'}
'''
names = ['John','Peter','Hanry','Lilith','kurt']
print({k:names[k] for k in range(5)})
'''
將list的值結合索引輸出新的dict
{0: 'John', 1: 'Peter', 2: 'Hanry', 3: 'Lilith', 4: 'kurt'}
'''
