from typing import Iterable


class MyClass:

    def __init__(self):
        self.name = "123"

    # def __getattr__(self, item):
    #     print(f"访问不存在的属性 {item}")
    #
    # def __getattribute__(self, item):
    #     print(f"访问属性： {item}")
    #
    # def __dir__(self) -> Iterable[str]:
    #     return ['name']


obj = MyClass()
# print(obj.x)
# print(obj.name)

print(dir(obj))

