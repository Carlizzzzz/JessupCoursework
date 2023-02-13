cars = ["Tesla", "Nio", "Solo", "Li", "BMW"]
years = [2002, 2005, 2010, 1995, 1999, 1987]


# 1
def addFavCar(arr, car):
    arr.append(car)
    print(car,"added to list")
    return arr

#2
def checkFavCar(arr,car):
    if arr.check(car):
        print(True)
    else:
        arr.append(car)
        print(car, "not found. Added as new item")
        return arr

#3
def countCars(arr):
    print( len(arr))

#4
def popCar(arr, index):
    poped = arr.pop(index)
    print(poped, "removed from the list at slot",index)
    return arr

#5
def reverseCar(arr):
    return arr.reverse()

#6
def myCars(arr,number):
    newCarList =[]
    for i in range(number):
        newCarList.append(arr[i])
    return newCarList

#7
def sumYears(arr):
    print (arr.sum())

#8
def countNewYears(arr):
    count=0
    for i in range(len(arr)):
        if(arr[i]>2000):
            count +=1
    print( count)

#9
def sortYears(arr):
    return arr.sort()

#10
def removeList(arr,index):
    arr.remove(index)
    return arr

print(addFavCar(cars,"Lexus"))
print(checkFavCar(cars,"Nio"))
print(countCars(cars))
print(popCar(cars,2))
print(reverseCar(cars))
print(myCars(cars,3))
print(sumYears(years))
print(countNewYears(years))
print(sortYears(years))
print(removeList(years,0))