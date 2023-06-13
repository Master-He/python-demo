from concurrent.futures import ThreadPoolExecutor


def worker():
    print('Worker')


# 线程池
with ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(5):
        executor.submit(worker)


# 第三方库
# import threadpool
#
# def worker(num):
#     print(f"Worker {num} started")
#     time.sleep(1)
#     print(f"Worker {num} finished")
#
# def main():
#     pool = threadpool.ThreadPool(3)
#     requests = threadpool.makeRequests(worker, range(3))
#     [pool.putRequest(req) for req in requests]
#     pool.wait()
#
# if __name__ == '__main__':
#     main()
