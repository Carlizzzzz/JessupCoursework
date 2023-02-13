from enum import Enum

def findCar(userInput):
    for i in CarBrand:
        if i.name == userInput:
            return myTuple[i.value-1]
    return "Not in database"

class CarBrand(Enum):
    AUDI = 1
    BENTLEY = 2
    HONDA = 3
    HYUNDAI = 4
    CHEVROLET = 5

myTuple = ("Germany","UK","Japan","Korea","US")

userInput = input("Please input a car brand")
print(findCar(userInput))

