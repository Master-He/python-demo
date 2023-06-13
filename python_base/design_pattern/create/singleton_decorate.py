import threading


def singleton(cls):
    instances = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class TestClass:

    def __init__(self, name):
        print("init()")
        self.name = name


if __name__ == '__main__':
    # 装饰器
    s1 = TestClass("foo")
    s2 = TestClass("bar")
    print(s1.name)  # foo
    print(s2.name)  # foo
    print(s1 is s2)  # True
