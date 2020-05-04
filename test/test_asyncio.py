import asyncio
import time

@asyncio.coroutine
def hello():
    print("hello world!")
    r = yield from asyncio.sleep(2)
    print("hello again")

loop = asyncio.get_event_loop()
print(time.localtime())
loop.run_until_complete(hello())
print(time.localtime())
loop.close()
print(time.localtime())
print("loop closed...")