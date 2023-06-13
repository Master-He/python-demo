# Python 3.7 引入了 async/await 语法，使得协程编程更加方便。在 Python 3.7 中，协程可以通过 asyncio 库来实现。
import asyncio


async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def main():
    await asyncio.gather(say_hello(), say_hello(), say_hello())


asyncio.run(main())
