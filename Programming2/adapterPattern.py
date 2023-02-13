import math

class MyMath:
    @staticmethod
    def sin(a):
        return math.sin(a)

    @staticmethod
    def cos(a):
        return math.cos(a)

    @staticmethod
    def asin(a):
        return math.asin(a)

    @staticmethod
    def acos(a):
        return math.acos(a)

class AdapterMath(MyMath):
    @staticmethod
    def sin(d):
        rad = math.radians(d)
        return math.sin(rad)

    @staticmethod
    def cos(d):
        rad = math.radians(d)
        return math.cos(rad)

    @staticmethod
    def asin(r):
        rad = math.asin(r)
        return math.degrees(rad)

    @staticmethod
    def acos(r):
        rad = math.acos(r)
        return math.degrees(rad)

print(AdapterMath.sin(90))
print(AdapterMath.asin(1))