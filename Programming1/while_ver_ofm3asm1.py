##1
def makeBig(makeItBig):
    i=0
    while i< len(makeItBig):
        if int(makeItBig[i]) > 0:
            makeItBig[i] = "big"
        i+=1
    return (makeItBig)


##2
def countingPositive(countPositives):
    count = 0
    i=0
    while i < len(countPositives):
        if int(countPositives[i]) > 0:
            count = count + 1
        i+=1
    countPositives[len(countPositives) - 1] = count
    return (countPositives)


##3
def findSum(sumTotal):
    sum = 0
    i = 0
    while i < len(sumTotal):
        sum = sum + sumTotal[i]
        i+=1
    return (sum)


##4
def findaverage(multiples):
    sum = 0
    i=0
    while i < len(multiples):
        sum = sum + multiples[i]
        i+=1
    return (sum / len(multiples))


##5
def findLength(length):
    return (len(length))


##6
def findMin(minimum):
    if (len(minimum) > 0):
        return (min(minimum))
    else:
        return (False)


##7
def findMax(maximum):
    if (len(maximum) > 0):
        return (max(maximum))
    else:
        return (False)


##8
def ultimateAnalyze(ult):
    analyze = [findSum(ult), findaverage(ult), findMin(ult), findMax(ult), findLength(ult)]
    return analyze


##9
def reverseList(reverse):
    temp = []
    i=0
    while i < len(reverse):
        temp.append(reverse[len(reverse) - 1 - i])
        i+=1
    return temp


def main():
    makeItBig = [-1, 3, 5, -5]
    print(makeBig(makeItBig))

    countPositives = [-1, 1, 1, 1]
    print(countPositives)

    sumTotal = [1, 2, 3, 4]
    print(findSum(sumTotal))

    multiples = [1, 2, 3, 4]
    print(findaverage(multiples))

    length = [1, 2, 3, 4]
    print(findLength(length))

    minimum = [-1, -4, 2, 5]
    print(findMin(minimum))

    maximum = [2, 35, 32, 666, 2]
    print(findMax(maximum))

    ult = [123, 2, 45, 667, 86]
    analyze = ultimateAnalyze(ult)
    print("Here is the analyze result of the array ", ult)
    print("Sum:", analyze[0], "Average:", analyze[1], "Min:", analyze[2], "Max:", analyze[3], "length:", analyze[4])

    reverse = [1, 2, 3, 4, 5]
    print(reverseList(reverse))


main()
