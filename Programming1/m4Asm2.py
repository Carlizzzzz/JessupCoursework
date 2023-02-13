# 10

## 3 % 4 == 0,
## 3 / 4 == 0
## 3+4  *  2 == 14
## 4-2+2 == 0
## These four statement fails beacuse 3%4 is 3 and 3/4 is 0.75 and 3+8 is 11 and 4-2+2 is 4

# 11
def compare(a, b):
    if (a > b):
        return 1
    elif (a < b):
        return -1
    else:
        return 0


# 12
def hypotenuse(a, b):
    return ((a ** 2 + b ** 2) ** 0.5)


# 13
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def intercept(x1, y1, x2, y2):
    return slope(x1, y1, x2, y2) * x2 * -1 + y2


# 14
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#15
def is_odd(n):
    if is_even(n):
        return False
    else:
        return True

#16
def is_factor(f,n):
    if n%f==0:
        return True
    else:
        return False

#17
def is_multiple(m,n):
    if is_factor(n,m):
        return True
    else:
        return False

#18
def f2c(t):
    return round((t-32)*5/9)

#19
def c2f(t):
    return round(t*9/5+32)



