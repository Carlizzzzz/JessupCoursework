##6
def findGrade(marks):
    if marks >= 75:
        return "First"
    elif marks >= 70:
        return "Upper Second"
    elif marks >= 60:
        return "Second"
    elif marks >= 50:
        return "Third"
    elif marks >= 45:
        return "F1 Supp"
    elif marks >= 40:
        return "F2"
    else:
        return "F3"


numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
           49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in range(0, len(numbers), 1):
    print(findGrade(numbers[i]))

##7
length = float(input("input the length"))
width = float(input("input the width"))
print("The length of hypotenuse is ", (length ** 2 + width ** 2) ** 0.5)

##8&9
a = float(input("length of side a:"))
b = float(input("length of side b:"))
c = float(input("length of side c:"))
sides = [a, b, c]
sorted(sides)
threshold = 1e-7
if abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < threshold:
    print("true")
else:
    print("false")

#14
numberList = [2, 3, 4]
sum=0
for i in range(0,len(numberList),1):
    sum = sum + numberList[i]**2
print(sum)