# Future 表示一个异步操作的结果，它的状态可以是 pending（等待执行）、running（正在执行）和 finished（执行完成）。
# 当异步操作完成后，Future 的状态会变为 finished，并且可以通过 result() 方法获取异步操作的结果。
# 在 asyncio 中，Future 通常由底层的协程或者回调函数创建，并且可以通过 asyncio.ensure_future() 函数将其转换为一个任务（Task）。

# Task 是对 Future 的进一步封装，它表示一个异步任务，可以由事件循环调度执行。
# 与 Future 不同的是，Task 可以设置回调函数，当任务执行完成时，回调函数会被自动调用。
# 在 asyncio 中，Task 通常由高层的协程创建，可以通过 asyncio.create_task() 函数创建。


import asyncio


async def coro():
    print('coro started')
    await asyncio.sleep(1)
    print('coro finished')
    return 'result'


async def main():
    print('main started')

    # 创建一个 Future 对象
    fut = asyncio.Future()

    # 将 coro 函数转换为一个 Task 对象
    task = asyncio.create_task(coro())

    # 设置回调函数
    task.add_done_callback(lambda t: fut.set_result(t.result()))

    # 等待 Future 对象的结果
    result = await fut
    print('main finished with result:', result)


asyncio.run(main())
