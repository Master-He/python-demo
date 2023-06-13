import threading


# 继承
class WorkerThread(threading.Thread):
    def run(self):
        print('Worker')


threads = []
for i in range(5):
    t = WorkerThread()
    threads.append(t)
    t.start()
