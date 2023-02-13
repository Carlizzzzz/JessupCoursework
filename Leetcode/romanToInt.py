def romanToInt(s):
    ref = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    numlist = []
    sum =0
    init = False
    for i in s:
        numlist.append(ref.get(i))
    for i in range(len(numlist)-1):
        if init:
            init = False
            continue
        if numlist[i] < numlist[i+1]:
            numlist[i] = numlist[i+1] - numlist[i]
            numlist[i+1] = 0
            init = True
    for i in numlist:
        sum = sum + i
    return sum


a = "III"
b = "MCMXCIV"
print(romanToInt(a))
print(romanToInt(b))

