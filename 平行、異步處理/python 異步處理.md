# python 異步處理

## asyncio模組

python 3.7以後支援 async/await 關鍵字來使用異步操作，需要釐清幾個名詞:

- 協程函數:返回一個 coroutine 對象的函數。協程函數可通過 async def 語句來定義，並可能包含 await、async for 和 async with 關鍵字。
  
- 協成物件: 協程是子例程的更一般形式。子例程可以在某一點進入並在另一點退出。協程則可以在許多不同的點上進入、退出和恢復。它們可通過 async def 語句來實現。 

- Task:任務 被用來設置日程以便 並發 執行協程。當一個協程通過 asyncio.create_task() 等函數被打包為一個 任務，該協程將自動排入日程準備立即運行

- 事件迴圈:事件循環，可以把他當做是一個while循環，這個while循環在周期性的運行並執行一些任務，在特定條件下終止循環。

``` python
# 引用asyncio module
import asyncio
import time
# 創建事件迴圈
loop = asyncio.get_event_loop()
# 定義協程函數
async def say_after(delay:float,text:str):
    print(f'say {text} start at {time.strftime("%H:%M:%S")}')
    await asyncio.sleep(delay)
    print(f'say {text} finished')
# 以asyncio.ensure_future 包裝協程物件為任務
task = asyncio.ensure_future(say_after(2.0,'hello'))
task2 = asyncio.ensure_future(say_after(1.0,'world'))
# 以事件迴圈執行任務，asyncio.wait會把多個task包裝成一個task
loop.run_until_complete(asyncio.wait([task,task2]))
```

結果
``` 
say hello start at 10:28:03
say world start at 10:28:03
say world finished
say hello finished
```

``` python
# 引用asyncio module
import asyncio
import time
# 創建事件迴圈
loop = asyncio.get_event_loop()
# 定義協程函數
async def say_after(delay:float,text:str):
    print(f'say {text} start at {time.strftime("%H:%M:%S")}')
    await asyncio.sleep(delay)
    print(f'say {text} finished')
# 定義一個main函數處理，使用await單純呼叫協程只會循序執行，而且不包裝成task就享受不到async的好處
async def main():
    print(f'start main() at {time.strftime("%H:%M:%S")}')
    await say_after(2.0,'hello')
    await say_after(1.0,'world')
    print(f'end main() at {time.strftime("%H:%M:%S")}')
# 以事件迴圈執行任務，asyncio.wait會把多個task包裝成一個task
loop.run_until_complete(main())
```

```
start main() at 11:12:27
say hello start at 11:12:27
say hello finished
say world start at 11:12:29
say world finished
end main() at 11:12:30
```

``` python
# 引用asyncio module
import asyncio
import time
# 創建事件迴圈
loop = asyncio.get_event_loop()
# 定義協程函數
async def say_after(delay:float,text:str):
    print(f'say {text} start at {time.strftime("%H:%M:%S")}')
    await asyncio.sleep(delay)
    print(f'say {text} finished')
# 包裝成task再使用就能享受到async的好處
async def main():
    task = asyncio.ensure_future(say_after(2.0,'hello'))
    task2 = asyncio.ensure_future(say_after(1.0,'world'))
    print(f'start main() at {time.strftime("%H:%M:%S")}')
    await task
    await task2
    print(f'end main() at {time.strftime("%H:%M:%S")}')
# 以事件迴圈執行任務，asyncio.wait會把多個task包裝成一個task
loop.run_until_complete(main())
```

```
start main() at 11:20:40
say hello start at 11:20:40
say world start at 11:20:40
say world finished
say hello finished
end main() at 11:20:42
```

## asyncio 非同步呼叫

以asyncio執行100次網路呼叫
``` python
import asyncio
import requests
import time

async def say_after(delay:float,text:str):
  start_t = time.time()
  await asyncio.sleep(delay)
  print(f"say {text} takes {time.time() - start_t} seconds.")

async def send_req(url):
  start_t = time.time()
  res = await asyncio.get_running_loop().run_in_executor(None,requests.get,url)
  print(f"Receive a response {res.status_code} takes {time.time() - start_t} seconds.")

url = 'https://www.google.com.tw/'
# coroutines = [say_after(2.0,'Hallo'), send_req(url)]
# coroutines = [say_after(2.0,'Hallo'), say_after(1.0,'world')]
coroutines = [send_req(url) for i in range(100)]
start_time = time.time()
asyncio.run(asyncio.wait(coroutines))
print(f'Whole loop takes {time.time() - start_time}')
```

```
//前面省略
Receive a response 200 takes 4.8970959186553955 seconds.
Whole loop takes 5.166743516921997
```

``` python
import asyncio
import requests
import time

loop = asyncio.get_event_loop()

async def say_after(delay:float,text:str):
  start_t = time.time()
  await asyncio.sleep(delay)
  print(f"say {text} takes {time.time()-start_t} seconds.")

async def send_req(url):
  start_t = time.time()
  res = await loop.run_in_executor(None,requests.get,url)
  print(f"Receive a response {res.status_code} takes {time.time()-start_t} seconds.")

url = 'https://www.google.com.tw/'
tasks = [send_req(url) for i in range(5)]
start_req_time = time.time()
loop.run_until_complete(asyncio.wait(tasks))
print(f'loop takes',time.time() - start_req_time,' second')
```

## aiohttp vs request: 非同步與同步網路呼叫

## 參考

[python doc:asyncio --- 异步 I/O](https://docs.python.org/zh-tw/3/library/asyncio.html)
[python的asyncio模組(一)：異步執行的好處](https://ithelp.ithome.com.tw/articles/10199385)
[asyncio异步编程，你搞懂了吗？](https://zhuanlan.zhihu.com/p/137057192)