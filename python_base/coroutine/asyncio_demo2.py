# Python 3.7 引入了 async/await 语法，使得协程编程更加方便。在 Python 3.7 中，协程可以通过 asyncio 库来实现。
import asyncio


async def my_coroutine():
    print("Starting coroutine")
    await asyncio.sleep(1)
    print("Coroutine completed")


async def main():
    task = asyncio.create_task(my_coroutine())
    await task


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
