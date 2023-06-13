class MyDict(dict):
    def __missing__(self, key):
        return f"Key {key} is not found in the dictionary."


d = MyDict(a=1, b=2)
print(d['a'])  # 1
print(d['c'])  # Key c is not found in the dictionary.
