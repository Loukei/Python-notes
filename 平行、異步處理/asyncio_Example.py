'''
示範python非同步模式(python 3.4 up)
單核並發(concurrency)模式，

需要釐清幾個概念

協程函數:返回一个 coroutine 对象的函数。协程函数可通过 async def 语句来定义，并可能包含 await、async for 和 async with 关键字。

協成物件:协程是子例程的更一般形式。 子例程可以在某一点进入并在另一点退出。 协程则可以在许多不同的点上进入、退出和恢复。 它们可通过 async def 语句来实现。 

Task:

事件迴圈:

[asyncio --- 异步 I/O](https://docs.python.org/zh-tw/3/library/asyncio.html)
[asyncio异步编程，你搞懂了吗？](https://zhuanlan.zhihu.com/p/137057192)
'''

# 引用asyncio module
import asyncio
import requests
import time

url = 'https://www.google.com.tw/'
# loop = asyncio.get_event_loop()
start_time = time.time()

async def say_after(delay:float,text:str):
    # t = time.time()
    # print(f"Say {text} after {delay} seconds...")
    await asyncio.sleep(delay)
    t = time.time()
    print(f"say {text} at {t-start_time} seconds.")

async def send_req(url):
    # t = time.time()
    # print("Send a request at",t-start_time,"seconds.")
    # res = await loop.run_in_executor(None,requests.get,url)
    res = await asyncio.get_running_loop().run_in_executor(None,requests.get,url)
    t = time.time()
    print(f"Receive a response {res.status_code} takes {t-start_time} seconds.")

# tasks = [send_req(url) for i in range(100)]
# tasks = []
# for i in range(100):
#     task = loop.create_task(send_req(url))
#     tasks.append(task)

# start_req_time = time.time()
# loop.run_until_complete(asyncio.wait(tasks))
# print(f'main() takes',time.time() - start_req_time,' second')

coroutines = [say_after(2.0,'Hallo'), send_req(url)]
# coroutines = [say_after(2.0,'Hallo'), say_after(1.0,'world')]
asyncio.run(asyncio.wait(coroutines))