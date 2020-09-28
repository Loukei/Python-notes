'''
callback函式範例
[typing --- 类型标注支持](https://docs.python.org/zh-cn/3/library/typing.html)
[Python中的類型標記](https://ocavue.com/python_typing.html#python-3-6-variable-annotations)
'''

'''
Example 1: python動態語言的特性可以讓你不用特意宣告就使用
'''
def callback1(a, b):
    print('Sum = {0}'.format(a+b))

def callback2(a):
    print('Square = {0}'.format(a**2))

def callback3():
    print('Hello, world!')

def main(callback=None, cargs=()):
    print('Calling callback.')
    if callable(callback):
        callback(*cargs)

print('---Example 1: Define a callback function and use callable() to check---')
main(callback1, cargs=(1, 2))
main(callback2, cargs=(2,))
main(callback3)
# main(5) # TypeError: 'int' object is not callable

'''
Example 2:使用typing.Callable定義一個callback函數
'''
from typing import Callable
def createList(size:int)->list:
    result = range(size)
    print(f'result = {result}, id = {id(result)}')
    return result
def execute(fun: Callable[[int],list]) -> None:
    print("Do something before callback...")
    list_b:list = fun(6)
    print(f'result = {list_b}')

print('---Example 2: Use typing.Callable---')
execute(createList)
