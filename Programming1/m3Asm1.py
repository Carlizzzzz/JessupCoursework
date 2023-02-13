##1
def makeBig(makeItBig):
    for i in range(0, len(makeItBig), 1):
        if int(makeItBig[i]) > 0:
            makeItBig[i] = "big"
    return (makeItBig)


##2
def countingPositive(countPositives):
    count = 0
    for i in range(0, len(countPositives), 1):
        if int(countPositives[i]) > 0:
            count = count + 1
    countPositives[len(countPositives) - 1] = count
    return (countPositives)


##3
def findSum(sumTotal):
    sum = 0
    for i in range(0, len(sumTotal), 1):
        sum = sum + sumTotal[i]
    return (sum)


##4
def findaverage(multiples):
    sum = 0
    for i in range(0, len(multiples), 1):
        sum = sum + multiples[i]
    return (sum / len(multiples))


##5
def findLength(length):
    return (len(length))


##6
def findMin(minimum):
    if (len(minimum) > 0):
        minValue = minimum[0]
        for i in range(0, len(minimum), 1):
            if minValue > minimum[i]:
                minValue = minimum[i]
        return (minValue)
    else:
        return (False)


##7
def findMax(maximum):
    if (len(maximum) > 0):
        maxValue = maximum[0]
        for i in range(0, len(maximum), 1):
            if maxValue > maximum[i]:
                maxValue = maximum[i]
        return (maxValue)
    else:
        return (False)


##8
def ultimateAnalyze(ult):
    analyze = [findSum(ult), findaverage(ult), findMin(ult), findMax(ult), findLength(ult)]
    return analyze


##9
def reverseList(reverse):
    temp = []
    for i in range(0, len(reverse), 1):
        temp.append(reverse[len(reverse) - 1 - i])
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
