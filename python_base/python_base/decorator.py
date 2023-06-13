def my_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before the method is called.")
        result = func(self, *args, **kwargs)
        print("After the method is called.")
        return result

    return wrapper


class MyClass:
    def __init__(self, value):
        self.value = value

    @my_decorator
    def my_method(self, x, y):
        return self.value + x + y


if __name__ == '__main__':
    obj = MyClass(10)
    result = obj.my_method(1, 2)
    print(result)
