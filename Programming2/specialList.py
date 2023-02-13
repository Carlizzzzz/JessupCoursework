class SpecialList:

    def __init__(self):
        self.list = []
        self.length = 0

    def __getitem__(self, key):
        if isinstance(key, int):
            if key < 0 or key > self.length - 1:
                raise IndexError
            return self.list[key]
        return TypeError

    def __setitem__(self, key, item):
        if isinstance(item, (int, str)):
            if isinstance(item, int):
                item = str(item)
            if self.length == 0 or item > self.list[self.length - 1]:
                self.list.append(item)
            else:
                for i in range(self.length):
                    if item <= self.list[i]:
                        self.list.insert(i, item)
            self.length += 1

    def __iter__(self):
        return SpecialListIter(self)

    def __reversed__(self):
        return SpecialListIter(self, False)

    def __len__(self):
        return self.length

    def __contains__(self, item):
        if isinstance(item, str):
            if item in self.list:
                return True
            else:
                return False
        raise TypeError

    def __delitem__(self, key):
        if isinstance(key, (int, str)):
            if isinstance(key, str):
                if key in self.list:
                    self.list.remove(key)
                else:
                    raise ValueError
            else:
                if key < 0 or key > self.length - 1:
                    raise IndexError
                else:
                    del self.list[key]
        else:
            raise TypeError

    def __str__(self):
        s = "["
        for j in self.list:
            s = s + j + ", "
        s = s + "]"
        return s


class SpecialListIter:
    def __init__(self, special, forward=True):
        self.special = special
        self.forward = forward
        if self.forward:
            self.index = 0
            self.dir = 1
        else:
            self.index = len(self.special) - 1
            self.dir = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.special) -1 or self.index < 0:
            raise StopIteration
        result = self.special[self.index]
        self.index += self.dir
        return result


list1 = SpecialList()
list1[0] = "dd"
list1[1] = "aa"

del list1["dd"]
print(list1)
