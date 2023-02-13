import types


def addAll(*args):
    sum = 0
    for i in args:
        if isinstance(i, (int, float)):
            sum += i
        elif isinstance(i, types.GeneratorType) and len(args) == 1:
            for j in i:
                sum += j
        else:
            raise TypeError
    return sum


def foo():
    lst = [1, 2, 3, 4, 5, 6]
    for i in lst:
        yield i


def foo2():
    pass


print(addAll(foo()))
print(addAll(1, 2, 3, 4, 5))
print(addAll(1.67, 1.34, 75.3))
print(addAll(1, 1.1, 2, 2.2))
try:
    print(addAll(foo2()))
except TypeError:
    print("Error occurred here!")
    pass
try:
    print(addAll("ste", 12, 3, 4, 5))
except TypeError:
    print("Error occurred here!")
    pass
try:
    print(addAll(foo(),foo()))
except TypeError:
    print("Error occurred here!")
    pass