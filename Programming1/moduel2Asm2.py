##1
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
value = int(input("input a number from 0-6"))
print(days[value])

##2
start = int(input("Start date"))
length = int(input("How long will it last?"))
value = (start+length)%7
print(days[value])

##3
    #1 a < b
    #2 a <= b
    #3 a <= 18  and  day != 3
    #4 a <= 18  and  day == 3

##4
    #1 True
    #2 False
    #3 False
    #4 False

##5
    # True
    # True
    # True
    # True
    # True
    # True
    # False
    # True