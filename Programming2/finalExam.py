import math


class sqrtWrapper:  # Part 1

    def __init__(self):
        self.sqrtStorage = {}

    def sqrt(self, num):
        if (isinstance(num, int) or isinstance(num, float)) and num >= 0:
            self.sqrtStorage[num] = math.sqrt(num)
            return self.sqrtStorage
        else:
            raise TypeError


sw = sqrtWrapper()
sw.sqrt(16.0)
sw.sqrt(9)
sw.sqrt(81)
print(sw.sqrt(100))
print("--------End of part 1-------- \n")


class sqrtAdapter():  # Part 2
    def sqrt(self, num):
        if isinstance(num, int) or isinstance(num, float):
            if num < 0:
                return str(math.sqrt(abs(num))) + "j"
            else:
                return math.sqrt(num)
        else:
            raise TypeError


sa = sqrtAdapter()
print(sa.sqrt(-81))
print(sa.sqrt(144))
print("--------End of Part 2-------- \n")


class sqrtFlyweight():  # Part 3
    def __init__(self):
        self.sqrtStorage = {}

    def sqrt(self, num):
        if (isinstance(num, int) or isinstance(num, float)) and num >= 0:
            sqrtValue = self.sqrtStorage.get(num)
            if not sqrtValue:
                sqrtValue = math.sqrt(num)
                self.sqrtStorage[num] = sqrtValue
                print("Value added!")
            else:
                print("Value already exist")
            return self.sqrtStorage
        else:
            raise TypeError


sf = sqrtFlyweight()
sf.sqrt(81)
sf.sqrt(9)
sf.sqrt(81)
print(sf.sqrt(16))
print("--------End of part 3 ---------\n")


class Command:  # Part 4
    commandList = []

    def Execute(self):
        pass

    @classmethod
    def AddCommand(cls, command):
        cls.commandList.append(command)

    @classmethod
    def ExecuteCommands(cls):
        sqrtList = []
        for i in cls.commandList:
            sqrtList.append(i.Execute())
        return sqrtList


class sqrtCommand(Command):
    def __init__(self, num):
        if (isinstance(num, int) or isinstance(num, float)) and num >= 0:
            self.num = num

    def Execute(self):
        return math.sqrt(self.num)


Command.AddCommand(sqrtCommand(4))
Command.AddCommand(sqrtCommand(16))
Command.AddCommand(sqrtCommand(49))
Command.AddCommand(sqrtCommand(36))
print(Command.ExecuteCommands())
print("--------End of part 4-------- \n")
