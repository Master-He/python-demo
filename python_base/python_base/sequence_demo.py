class MyList:
    def __init__(self, *args):
        self.data = list(args)

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            return self.data[start:stop:step]
        else:
            return self.data[index]


if __name__ == '__main__':
    mylist = MyList(1, 2, 3, 4, 5)
    print(mylist[1:3])  # 输出 [2, 3]

    # 列表推导式
    print([x * x for x in range(1, 11)])
    # 生成器推导式
    print((x * x for x in range(1, 11)))
    # 字典推导式
    print({x: x*x for x in range(1, 11)})
    # 集合推导式
    print({x * x for x in range(1, 11)})
