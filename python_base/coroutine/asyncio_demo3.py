# Python 3.7 引入了 async/await 语法，使得协程编程更加方便。在 Python 3.7 中，协程可以通过 asyncio 库来实现。
import asyncio


async def coroutine_1():
    print("Starting coroutine 1")
    await asyncio.sleep(1)
    print("Coroutine 1 completed")


async def coroutine_2():
    print("Starting coroutine 2")
    await asyncio.sleep(2)
    print("Coroutine 2 completed")


async def main():
    await asyncio.gather(coroutine_1(), coroutine_2())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
