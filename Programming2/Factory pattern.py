class ComplexNumber:
    def __init__(self, real, virtual):
        self.real = real
        self.virtual = virtual

    def add(self, number):
        sumReal = self.real + number.real
        sumVirtual = self.virtual + number.virtual
        return ComplexNumber(sumReal, sumVirtual)

    def subtract(self, number):
        diffReal = self.real - number.real
        diffVirtual = self.virtual - number.virtual
        return ComplexNumber(diffReal, diffVirtual)

    def multiply(self, number):
        prodReal = self.real * number.real - self.virtual * number.virtual
        prodVirtual = self.real * number.virtual + self.virtual * number.real
        return ComplexNumber(prodReal, prodVirtual)

    def divide(self, number):
        facReal = (self.real * number.real + self.virtual * number.virtual) / (
                    number.real * number.real + number.virtual * number.virtual)
        facVirtual = (self.virtual * number.real - self.real * number.virtual) / (
                    number.real * number.real + number.virtual * number.virtual)
        return ComplexNumber(facReal, facVirtual)

    def __str__(self):
        if self.real !=0:
            return str(self.real)+str(self.virtual)+"i"
        else:
            return str(self.virtual)+"i"

class Number:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

class Factory:
    def __init__(self, num):
        self.num = num

    def create(self):
        plus_or_minus = 0
        if "i" in self.num:
            for j in range(len(self.num)):
                if self.num[j] == "+" or self.num[j]=="-":
                    plus_or_minus = j+1
            if plus_or_minus != 0:
                return ComplexNumber(self.num[0:plus_or_minus - 1], self.num[plus_or_minus-1:len(self.num) - 1])
            else:
                return ComplexNumber(0,self.num[plus_or_minus:len(self.num) - 1])
        else:
            try:
                return Number(int(self.num))
            except ValueError:
                print("Error!")
                pass




f = Factory("532")
f2 = Factory("123+4535i")
f3 = Factory("123+123")
f4 = Factory("213i")
print(f.create(), "type =", type(f.create()))
print(f2.create(), "type =", type(f2.create()))
print(f3.create(), "type =", type(f3.create()))
print(f4.create(), "type =", type(f4.create()))


