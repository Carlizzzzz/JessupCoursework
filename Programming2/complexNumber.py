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




