import threading


def worker():
    print('Worker')


threads = []
for i in range(5):
    # target方式
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
