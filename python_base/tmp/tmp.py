import math


class Tmp:

    def __init__(self):
        self.dict = dict()

    def __getitem__(self, item):
        pass
        # print("get item")
        # if item in self.dict:
        #     return self.dict[item]
        # else:
        #     return None

    def __setitem__(self, key, value):
        print("set item")
        self.dict[key] = value

    def __delitem__(self, key):
        del self.dict[key]

    def __contains__(self, item):
        return item in self.dict

    def __len__(self):
        return len(self.dict)

    def __missing__(self, key):
        print(f"没有这个键: {key}")


if __name__ == '__main__':
    t = Tmp()

    for i in range(20):
        print(math.pow(2, i))

    print(math.pow(2, 15))
