import threading


class Singleton:
    _lock = threading.Lock()
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name
        print("init()")  # 进来两次


if __name__ == '__main__':
    s1 = Singleton("foo")
    s2 = Singleton("bar")

    print(s1.name)  # bar
    print(s2.name)  # bar
    print(s1 is s2)  # True

