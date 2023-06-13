# Python 3.7 引入了 async/await 语法，使得协程编程更加方便。在 Python 3.7 中，协程可以通过 asyncio 库来实现。

import asyncio


async def my_coroutine():
    print("start coroutine")
    await asyncio.sleep(1)
    print("coroutine completed")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_coroutine())

