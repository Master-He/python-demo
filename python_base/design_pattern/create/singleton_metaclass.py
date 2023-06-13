import threading


class SingletonMeta(type):
    _instance = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    s1 = Singleton("foo")
    s2 = Singleton("bar")
    print(s1.name)  # foo
    print(s2.name)  # foo
    print(s1 is s2)   # True
