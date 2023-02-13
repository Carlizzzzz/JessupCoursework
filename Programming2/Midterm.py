class Step:
    def __init__(self, count, name):
        if not isinstance(count, (float,int)):
            raise TypeError
        if not isinstance(name, str):
            raise TypeError
        self.count = count
        self.name = name

    def __str__(self):
        return "Add {0} {1}".format(self.count, self.name)


class Recipe:
    def __init__(self):
        self.steps = []

    def __len__(self):
        return len(self.steps)

    def __setitem__(self, key, item):
        if type(item)is not list:
            if isinstance(item, Step):
                self.addStep = item
            else:
                raise TypeError

        if type(item) is list and len(item) == 2:
            if isinstance(item[0], (int,float)):
                if isinstance(item[1], str):
                    self.addStep = Step(item[0], item[1])
                else:
                    raise TypeError
            else:
                raise TypeError

        if type(item) is list and len(item) > 2:
            raise SyntaxError

        if isinstance(key, int):
            if (key < 0 - len(self.steps)) or (key > len(self.steps) - 1):
                raise IndexError
            else:
                self.steps[key] = self.addStep
        else:
            raise TypeError

    def __getitem__(self, key):
        if isinstance(key, int):
            if (key < 0 - len(self.steps)) or (key > len(self.steps) - 1):
                raise IndexError
            else:
                return self.steps[key]
        else:
            raise TypeError

    def __delitem__(self, key):
        if isinstance(key, int):
            if (key < 0 - len(self.steps)) or (key > len(self.steps) - 1):
                raise IndexError
            else:
                del self.steps[key]
        raise TypeError

    def __add__(self, other):
        if isinstance(other, Step):
            self.steps.append(other)
            return self
        else:
            return NotImplemented

    def __str__(self):
        s =""
        for j in self.steps:
            s = s + str(j) + ", "
        return s



#test code
a = Step(2, "egg")
b= Step(3,"fish")
r = Recipe()
r = r+a+b
print(r)
r = r + a
print(r)
r[0] = [2,"orange"]
print(r)
for i in r:
    print(i)
try:
    c = Step("int", 3)
except TypeError:
    print("error")
try:
    c = Recipe("int", 3)
except TypeError:
    print("error")
