import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor


async def compute_in_threadpool(executor, func, *args):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, func, *args)
    return result


def blocking_io():
    # 使用阻塞 I/O 操作
    print("使用阻塞 I/O 操作", threading.current_thread().getName())
    time.sleep(1)
    print("end 阻塞IO", threading.current_thread().getName())


def cpu_bound():
    # 使用 CPU 密集型操作
    print("CPU 密集型操作", threading.current_thread().getName())
    time.sleep(1)
    print("end CPU", threading.current_thread().getName())


async def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        # 并发执行阻塞 I/O 操作
        await asyncio.gather(
            compute_in_threadpool(executor, blocking_io),
            compute_in_threadpool(executor, blocking_io),
            compute_in_threadpool(executor, blocking_io),
        )

        # 并发执行 CPU 密集型操作
        # await asyncio.gather(
        #     compute_in_threadpool(executor, cpu_bound),
        #     compute_in_threadpool(executor, cpu_bound),
        #     compute_in_threadpool(executor, cpu_bound),
        # )


if __name__ == '__main__':
    asyncio.run(main())
