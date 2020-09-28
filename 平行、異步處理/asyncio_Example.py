'''
示範python非同步模式(python 3.4 up)
單核並發(concurrency)模式，
[asyncio --- 异步 I/O](https://docs.python.org/zh-tw/3/library/asyncio.html)
[asyncio异步编程，你搞懂了吗？](https://zhuanlan.zhihu.com/p/137057192)
'''
import asyncio

# 定義協程
async def task(id:int,wait:int = 0):
    print(f"Task {id} start...")
    await asyncio.sleep(wait)
    print(f"... Task {id} finished")

tasks = [asyncio.ensure_future(task(0,3)),
            asyncio.ensure_future(task(1,1)),
            asyncio.ensure_future(task(2,2))]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
