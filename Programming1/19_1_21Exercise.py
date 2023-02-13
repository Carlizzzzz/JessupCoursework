import math
##compound interest
p = float(input("insert p"))
r = float(input("insert r"))
t = float(input("insert t"))
n = float(input("insert n"))
print("The amount is",p*((1+r/n)**(n*t)))

##rectangle area and perimeter
width = float(input("What's the width?"))
height = float(input("What's the height?"))
print("The area is",height*width,"and the perimeter is",height*2 + width*2)

##mortgage payment
p = float(input("insert p"))
i = float(input("insert i"))
n = float(input("insert n"))
print("The mortgage payment is", p*(i*((1+i)**n))/((1+i)**n-1))

##Circle area
radius = float(input("insert radius"))
print("Area is", math.pi*(radius**2))