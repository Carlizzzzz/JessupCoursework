legacy = float
legacy = None


def plus(a: float, b: float):
    global legacy
    legacy = a + b
    return legacy


def minus(a: float, b: float):
    global legacy
    legacy = a - b
    return legacy


def times(a: float, b: float):
    global legacy
    legacy = a * b
    return legacy


def divide(a: float, b: float):
    if b == 0:
        return "cannot divide by 0"
    global legacy
    legacy = a / b
    return legacy


def cal():
    print("input: ")
    x = input()
    num = [float, float]
    pointer = 0
    count = 1
    case = int
    if x[0:1].isnumeric() or (x[0:1] == "-" and legacy is None):
        for i in range(1, len(x)):
            if pointer > 1:
                print("too much")
                cal()
            if x[i:i + 1].isnumeric():
                count += 1
            elif x[i:i + 1] == ".":
                count += 1
                continue
            else:
                num[pointer] = float(x[0:count])
                count = 0
                pointer += 1
                if x[i:i + 1] == "+":
                    case = 0
                elif x[i:i + 1] == "-":
                    case = 1
                elif x[i:i + 1] == "*":
                    case = 2
                elif x[i:i + 1] == "/":
                    case = 3
                else:
                    print("invalid symbol")
                    cal()
        num[pointer] = float(x[len(x) - count:len(x)])
    elif not(x[0:1] == "+" or x[0:1] == "-" or x[0:1] == "*" or x[0:1] == "/"):
        print("invalid symbol")
        cal()
    elif legacy is None:
        print("no history found")
        cal()
    else:
        if x[0:1] == "+":
            num[0] = legacy
            num[1] = float(x[1:len(x)])
            print(num)
            case = 0
        elif x[0:1] == "-":
            num[0] = legacy
            num[1] = float(x[1:len(x)])
            case = 1
        elif x[0:1] == "*":
            num[0] = legacy
            num[1] = float(x[1:len(x)])
            case = 2
        elif x[0:1] == "/":
            num[0] = legacy
            num[1] = float(x[1:len(x)])
            case = 3
    if case == 0:
        print(plus(num[0], num[1]))
        cal()
    elif case == 1:
        print(minus(num[0], num[1]))
        cal()
    elif case == 2:
        print(times(num[0], num[1]))
        cal()
    elif case == 3:
        print(divide(num[0], num[1]))
        cal()

    print("invalid input")
    cal()


cal()
