class Command:
    commandList = []

    def Execute(self):
        pass

    @classmethod
    def AddCommand(cls, command):
        cls.commandList.append(command)

    @classmethod
    def ExecuteCommands(cls):
        for i in cls.commandList:
            total = i.Execute()
        return total

    @classmethod
    def Undo(cls):
        cls.commandList.pop()
        cls.ExecuteCommands()

class Add(Command):
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def Execute(self):
        return self.a + self.b


class Sub(Command):
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def Execute(self):
        return self.a - self.b


class Times(Command):
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def Execute(self):
        return self.a * self.b


class Div(Command):
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def Execute(self):
        return self.a / self.b

class Set(Command):
    def __init__(self,a):
        self.a = int(a)

    def Execute(self):
        return self.a

method = ""
firstTime = True
while method != "end":
    method = input("What you want to do? (1-Add, 2-Subtract, 3-times, 4-divide, 5-undo, end-exit program)")
    if method not in ["1","2","3","4","5", "end"]:
        print("invalid input")
    elif method == "end":
        break
    else:
        if firstTime:
            a = input("first number")
            Command.AddCommand(Set(a))
            firstTime = False
        if method == "1":
            b = input("following number")
            print(type(b))
            Command.AddCommand(Add(Command.ExecuteCommands(),b))
        elif method == "2":
            b = input("following number")
            Command.AddCommand(Sub(Command.ExecuteCommands(),b))
        elif method == "3":
            b = input("following number")
            Command.AddCommand(Times(Command.ExecuteCommands(),b))
        elif method == "4":
            b = input("following number")
            Command.AddCommand(Div(Command.ExecuteCommands(),b))
        else:
            Command.Undo()
        print(Command.ExecuteCommands())


