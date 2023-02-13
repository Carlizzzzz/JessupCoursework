##1
a = "All"
b = "work"
c = "and"
d = "no"
e = "play"
f = "makes"
g = "Jack"
h = "a"
i = "dull"
j = "boy"
print(a, b, c, d, e, f, g, h, i, j)

##2
print(6 * (1 - 2))

##4
bruce = 6
print(bruce + 4)

##5
p = float(input("insert your principal amount"))
r = float(input("insert the interest rate"))
t = float(input("insert the number of years"))
n = float(input("insert frequency that the interest is paid out per year"))
print("The amount is", p * ((1 + r / n) ** (n * t)))

##6 Since we cannot divide a number by 0 so anyNum%0 will be math error

##7
time = (14 + 51) % 24
print("the time that the alarm will go on will be ", time, ":00")

##8
t_now = int(input("input time now(24hours)"))
t_wait = int(input("time need to wai"))
time = (t_now + t_wait) % 24
print("the time that the alarm will go on will be ", time, ":00")
